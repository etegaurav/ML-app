from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
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
    response = util.predicted_price(Location, Desired_sqft, Bedrooms, Bathrooms)
    return render_template('index.html', prediction_text= 'Estimated price is Rs {} lakhs'.format(str(response)))


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_objects()
    app.run(debug=True)
