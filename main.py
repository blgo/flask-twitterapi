from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template

from twitterapi.gettwitts import *
from twitterapi.geolocation import * 

from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

from os import getenv
     
app = Flask(__name__)

app.config['GOOGLEMAPS_KEY'] = os.getenv('GOOGLEMAPS_KEY')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

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


    try:
        gmmarkers = GoogleMapsMarkers()
        gmmarkers.find_coordinates(twitts.statuses)
    except Exception as error:
        return render_template("error.html", error=str(error))
    # creating a map in the view
    if len(gmmarkers.markers) > 0:
        try:
            sndmap = Map(
                identifier="sndmap",
                lat=gmmarkers.markers[0].get('lat'),
                lng=gmmarkers.markers[0].get('lng'),
                style="height:300px;width:90%;margin:0;",
                zoom=2,
                markers=gmmarkers.markers
            )
        except Exception as error:
            return render_template("error.html", error=str(error))
    else:
        sndmap = Map(
            identifier="sndmap",
            lat=0,
            lng=0,
            style="height:300px;width:90%;margin:0;",
            zoom=2,
        )
    return render_template("index.html", twitts=twitts, sndmap=sndmap)


if __name__ == "__main__":
    app.run()
