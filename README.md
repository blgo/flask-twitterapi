# flask-twitterapi

Simple Flask web app, which integrates a search string for geolocalization and display twitts on top of GoogleMaps.

## Setup

* Compatible with Python3.6
* Install requerimets on requirements.txt
* Pupulate your .env file with the following variables
    * `twitteruser = ''` # Twitter user from which we want to get twitts: "screen_name"
    * `consumer_key = ''` # go [here](https://apps.twitter.com/app/new) and create your twitter app
    * `consumer_secret = ''` # go to "manage keys and access tokens" to see your consumer_secret key
    * `access_token_key = ''` # download, run [this script](https://github.com/bear/python-twitter/blob/master/get_access_token.py) and follow inscructions
    * `access_token_secret = ''` 
    * `GOOGLEMAPS_KEY = ''` # [get here](https://developers.google.com/maps/documentation/javascript/get-api-key)
* Run `python main.py`

## Features

* Mobile devices responsive desing with Bootstrap
* Displays the geolocalised twitts in GoogleMaps, each marker includes a text box with the twitter link to the article or twitt Id.

## Docker image

### Build Docker image

`docker build . -t flask-twitterapi:latest`

### Run Docker image

`docker run --rm -p 80:80 flask-twitterapi:latest`
