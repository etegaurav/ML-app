import json
import pickle
import numpy as np

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


if __name__ == "__main__":
    print("Starting flask server to begin House price prediction...")
    load_objects()
    print(get_location_names())
    print(predicted_price("vishveshwarya layout", 1000, 2, 2))
    print(predicted_price("2nd phase judicial layout", 1000, 2, 2))



