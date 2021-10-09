from flask import Flask,jsonify
from geopy.geocoders import Nominatim
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route("/<place>")
def hello_world(place):
    geolocator = Nominatim(user_agent="greatlygravitate")
    location = geolocator.geocode(str(place))
    return jsonify(str(location.latitude) + "," + str(location.longitude))

@app.route("/")
def index():
    return "LatLong is a latitude and longitude finding api."
