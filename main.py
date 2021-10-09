from flask import Flask,jsonify,render_template
from geopy.geocoders import Nominatim
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route("/find/<place>/")
def hello_world(place):
    geolocator = Nominatim(user_agent="greatlygravitate")
    location = geolocator.geocode(str(place))
    return jsonify(str(location.latitude) + "," + str(location.longitude))

@app.route("/")
def index():
    return """
        
This is LatLong API.<br>
This api is meant for finding the Latitude and Longitutde of a location.<br>
Start by typing a address like this: <code>https://latlong.pythonanywhere.com/find/{location}</code>
    """
