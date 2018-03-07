Live demo: https://ppw2v8syjg.execute-api.eu-west-1.amazonaws.com/dev
# flask-twitterapi

Simple Flask web app, which integrates a search string for geolocalization and display twitts on top of GoogleMaps.

## Setup

* Compatible with Python3.6
* Install requirimets: `$ pip -r requirements/base.txt`
* Pupulate your .env file with the following variables
    * `export twitteruser=''` # Twitter user from which we want to get twitts: "screen_name"
    * `export consumer_key=''` # go [here](https://apps.twitter.com/app/new) and create your twitter app
    * `export consumer_secret=''` # go to "manage keys and access tokens" to see your consumer_secret key
    * `export access_token_key=''` # download, run [this script](https://github.com/bear/python-twitter/blob/master/get_access_token.py) and follow instructions
    * `export access_token_secret=''` 
    * `export GOOGLEMAPS_KEY=''` # [get here](https://developers.google.com/maps/documentation/javascript/get-api-key)
* Run `. .env; python main.py`

## Features

* Mobile devices responsive desing with Bootstrap
* Displays the geolocalised twitts in GoogleMaps, each marker includes a text box with the twitter link to the article or twitt Id.

## Docker image

### Build or Download Docker image

`docker build . -t flask-twitterapi:latest`

OR

`docker pull blgo/flask-twitterapi:latest` 

### Run Docker image

`docker run --rm -v ./.env:/app/.env -p 80:80 flask-twitterapi:latest`


### TODO
* ~~Optimise country search, analyse performance using Qcachegrind~~
* Make util fuction for analysing performance based on:
`python -m cProfile -o profile_data.pyprof tests/gettwitts_tests.py`
`python -m pyprof2calltree -i profile_data.pyprof -k`
&&
https://gitlab.com/blgo/learn-more-python-the-hard-way/blob/master/ex6-find/find.py comand line arguments parser.
* Configuration management: http://flask.pocoo.org/docs/0.12/config/
    * fix unittests debugging (enviroment variables inyection does not work)
    * Amend README accordingly
* ~~Create .env and zappa_setting example files~~
* Test Docker image, amend Dockerhub README
* Add https URLs for Twitter images
* Autodeploy to AWS LAMBDA using Travis only for master
* Sanitaze dependencies
* Limit Zappa IAM user and roles privileges (edit example config file)