from flask import Flask, request, jsonify, render_template
import json
import pickle
import numpy as np

app = Flask(__name__)

__location = None
__data_columns = None
__model = None


def get_location_names():
    return __location


def load_objects():
    global __location
    global __data_columns
    global __model
    # defining the context manager for loading the data in the columns.json and pickle
    # (refer to corey schafer reading/writing file tutorials)
    with open('columns.json', 'r') as f:
        __data_columns = json.load(f)['data.columns']
        __location = __data_columns[3:]
    with open('housing_price_predict_model.pickle', 'rb') as f1:
        __model = pickle.load(f1)


def predicted_price(location, sqft, bed, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bed
    if loc_index > 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0], 2)
    



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/name_return', methods=['POST'])
def name_return():
    posted_data = request.get_json()
    data = posted_data['data']
    return jsonify(str("Successfully stored "+ str(data)))


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    Desired_sqft = float(request.form['Desired_sqft'])
    Location = request.form['Location']
    Bedrooms = int(request.form['Bedrooms'])
    Bathrooms = int(request.form['Bathrooms'])
    response = predicted_price(Location, Desired_sqft, Bedrooms, Bathrooms)
    return render_template('index.html', prediction_text= 'Estimated price is Rs {} lakhs'.format(str(response)))


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    load_objects()
    app.run(debug=True)
