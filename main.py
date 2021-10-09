from flask import Flask,jsonify
from geopy.geocoders import Nominatim

app = Flask(__name__)

@app.route("/<place>")
def hello_world(place):
    geolocator = Nominatim(user_agent="greatlygravitate")
    location = geolocator.geocode(str(place))
    return jsonify(str(location.latitude) + "," + str(location.longitude))
