from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template

from twitterapi.gettwitts import *
from twitterapi.importcsv import *
from twitterapi.geolocation import * 

from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
     
app = Flask(__name__)

app.config['GOOGLEMAPS_KEY'] = "AIzaSyDytwPN4A0o6hkgTvaVyViBFeAkJbHYdDQ"
GoogleMaps(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    # "setup" the session with starting values
    twitts = Twitts()
    try:
        twitts.authenticate()
        twitts.api.VerifyCredentials()
    except Exception:
        return render_template("error401.html")
    try:
        twitts.get_twitts()
    except Exception as error:
        return render_template("error.html", error=str(error))


    countries = load_countries()
    gmmarkers = GoogleMapsMarkers()
    gmmarkers.find_coordinates(twitts.statuses, countries)


    # creating a map in the view
    sndmap = Map(
        identifier="sndmap",
        lat=37.4419,
        lng=-122.1419,
        fit_markers_to_bounds = True,
        markers=gmmarkers.markers
    )
    return render_template("index.html", twitts=twitts, sndmap=sndmap)


app.secret_key = '1Ai9Mk1fXnkN3VN1yTw445QZDokF4b'


if __name__ == "__main__":
     app.run(debug=True)
