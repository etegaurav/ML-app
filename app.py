from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)
__data_columns = ["total_sqft", "bath", "bedrooms", "1st block jayanagar", "1st phase jp nagar",
                  "2nd phase judicial layout", "2nd stage nagarbhavi", "5th block hbr layout", "5th phase jp nagar",
                  "6th phase jp nagar", "7th phase jp nagar", "8th phase jp nagar", "9th phase jp nagar", "aecs layout",
                  "abbigere", "akshaya nagar", "ambalipura", "ambedkar nagar", "amruthahalli", "anandapura",
                  "ananth nagar", "anekal", "anjanapura", "ardendale", "arekere", "attibele", "beml layout",
                  "btm 2nd stage", "btm layout", "babusapalaya", "badavala nagar", "balagere", "banashankari",
                  "banashankari stage ii", "banashankari stage iii", "banashankari stage v", "banashankari stage vi",
                  "banaswadi", "banjara layout", "bannerghatta", "bannerghatta road", "basavangudi",
                  "basaveshwara nagar", "battarahalli", "begur", "begur road", "bellandur", "benson town",
                  "bharathi nagar", "bhoganhalli", "billekahalli", "binny pete", "bisuvanahalli", "bommanahalli",
                  "bommasandra", "bommasandra industrial area", "bommenahalli", "brookefield", "budigere",
                  "cv raman nagar", "chamrajpet", "chandapura", "channasandra", "chikka tirupathi", "chikkabanavar",
                  "chikkalasandra", "choodasandra", "cooke town", "cox town", "cunningham road", "dasanapura",
                  "dasarahalli", "devanahalli", "dodda nekkundi", "doddaballapur", "doddakallasandra", "doddathoguru",
                  "domlur", "dommasandra", "epip zone", "electronic city", "electronic city phase ii",
                  "electronics city phase 1", "frazer town", "gm palaya", "garudachar palya", "giri nagar",
                  "gollarapalya hosahalli", "gottigere", "green glen layout", "gubbalala", "gunjur", "hal 2nd stage",
                  "hbr layout", "hrbr layout", "hsr layout", "haralur road", "harlur", "hebbal", "hebbal kempapura",
                  "hegde nagar", "hennur", "hennur road", "hoodi", "horamavu agara", "horamavu banaswadi", "hormavu",
                  "hosa road", "hosakerehalli", "hoskote", "hosur road", "hulimavu", "isro layout", "itpl",
                  "iblur village", "indira nagar", "jp nagar", "jakkur", "jalahalli", "jalahalli east", "jigani",
                  "judicial layout", "kr puram", "kadubeesanahalli", "kadugodi", "kaggadasapura", "kaggalipura",
                  "kaikondrahalli", "kalena agrahara", "kalyan nagar", "kambipura", "kammanahalli", "kammasandra",
                  "kanakapura", "kanakpura road", "kannamangala", "karuna nagar", "kasavanhalli", "kasturi nagar",
                  "kathriguppe", "kaval byrasandra", "kenchenahalli", "kengeri", "kengeri satellite town",
                  "kereguddadahalli", "kodichikkanahalli", "kodigehaali", "kodigehalli", "kodihalli", "kogilu",
                  "konanakunte", "koramangala", "kothannur", "kothanur", "kudlu", "kudlu gate", "kumaraswami layout",
                  "kundalahalli", "lb shastri nagar", "laggere", "lakshminarayana pura", "lingadheeranahalli",
                  "magadi road", "mahadevpura", "mahalakshmi layout", "mallasandra", "malleshpalya", "malleshwaram",
                  "marathahalli", "margondanahalli", "marsur", "mico layout", "munnekollal", "murugeshpalya",
                  "mysore road", "ngr layout", "nri layout", "nagarbhavi", "nagasandra", "nagavara", "nagavarapalya",
                  "narayanapura", "neeladri nagar", "nehru nagar", "ombr layout", "old airport road", "old madras road",
                  "padmanabhanagar", "pai layout", "panathur", "parappana agrahara", "pattandur agrahara",
                  "poorna pragna layout", "prithvi layout", "r.t. nagar", "rachenahalli", "raja rajeshwari nagar",
                  "rajaji nagar", "rajiv nagar", "ramagondanahalli", "ramamurthy nagar", "rayasandra", "sahakara nagar",
                  "sanjay nagar", "sarakki nagar", "sarjapur", "sarjapur  road", "sarjapura - attibele road",
                  "sector 2 hsr layout", "sector 7 hsr layout", "seegehalli", "shampura", "shivaji nagar",
                  "singasandra", "somasundara palya", "sompura", "sonnenahalli", "subramanyapura", "sultan palaya",
                  "tc palaya", "talaghattapura", "thanisandra", "thigalarapalya", "thubarahalli", "tindlu",
                  "tumkur road", "ulsoor", "uttarahalli", "varthur", "varthur road", "vasanthapura", "vidyaranyapura",
                  "vijayanagar", "vishveshwarya layout", "vishwapriya layout", "vittasandra", "whitefield",
                  "yelachenahalli", "yelahanka", "yelahanka new town", "yelenahalli", "yeshwanthpur"]
__location = __data_columns[3:]
with open('housing_price_predict_model.pickle', 'rb') as f1:
    __model = pickle.load(f1)


def predicted_price(location, sqft, bed, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    print(x)
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
    response = jsonify({"location":__location})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    desired_sqft = float(request.form['Desired_sqft'])
    location = request.form['Location']
    bedrooms = int(request.form['Bedrooms'])
    bathrooms = int(request.form['Bathrooms'])
    response = predicted_price(location, desired_sqft, bedrooms, bathrooms)
    return render_template('index.html', prediction_text='Estimated price is Rs {} lakhs'.format(str(response)))


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    app.run(debug=True)
