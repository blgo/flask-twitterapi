# flask-twitterapi

Simple Flask web app, which integrates a search string for geolocalization and display twitts on top of GoogleMaps.

## Setup

* Compatible with Python3.6
* Install requerimets on requirements.txt
* Pupulate your .env file with the following variables
    * `twitteruser = ''`
    * `consumer_key = ''`
    * `consumer_secret = ''`
    * `access_token_key = ''`
    * `access_token_secret = ''`
    * `GOOGLEMAPS_KEY = ''`
* Run `python main.py`

## Features

* Mobile devices responsive desing with Bootstrap
* Displays the geolocalised twitts in GoogleMaps, each marker includes a text box with the twitter link to the article or twitt Id.

## Docker image

### Build Docker image

`docker build . -t flask-twitterapi:latest`

### Run Docker image

`docker run --rm -p 80:80 flask-twitterapi:latest`
