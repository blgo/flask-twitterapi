# flask-twitterapi

Simple Flask web app, which integrates a hashtag search for geolocalization and displays twitts by country on GoogleMaps.

## Live demo

https://ppw2v8syjg.execute-api.eu-west-1.amazonaws.com/dev

## Setup

* Install requirimets: `$ pip -r requirements/base.txt`
* Pupulate your .env file with the following lines (see config_examples)
    * export `twitteruser=''` # Twitter user from which we want to get twitts: "screen_name"
    * export `consumer_key=''` # go [here](https://apps.twitter.com/app/new) and create your twitter app
    * export `consumer_secret=''` # go to "manage keys and access tokens" to see your consumer_secret key
    * export `access_token_key=''` # download, run [this script](https://github.com/bear/python-twitter/blob/master/get_access_token.py) and follow instructions
    * export `access_token_secret=''` 
    * export `GOOGLEMAPS_KEY=''` # [get here](https://developers.google.com/maps/documentation/javascript/get-api-key)
    * export `SECRET_KEY=''` # Randomly generated string used by Flask for your cookies and other stuff
* Run `. .env; python main.py`

## Features

* Responsive Mobile devices desing with Bootstrap
* Displays the geolocalised twitts in GoogleMaps, each marker includes a text box with the twitter link to the article or twitt Id.

## Docker image

### Build or Download Docker image

Build your local Docker image

`docker build . -t flask-twitterapi:latest`

OR download from Docker hub

`docker pull blgo/flask-twitterapi:latest` 

### Run Docker image

Rename your .env file to "env" and run:
```
. .env; \
docker run --rm --name flask-twitterapi-run \
-e twitteruser="${twitteruser}" \
-e consumer_key="${consumer_key}" \
-e consumer_secret="${consumer_secret}" \
-e access_token_key="${access_token_key}" \
-e access_token_secret="${access_token_secret}" \
-e GOOGLEMAPS_KEY="${GOOGLEMAPS_KEY}" \
-e SECRET_KEY="${SECRET_KEY}" \
-p 80:80 flask-twitterapi:latest

```

Access the application: http://localhost

### TODO
* ~~Optimise country search, analyse performance using Qcachegrind~~
* ~~Create .env and zappa_setting example files~~
* ~~Test Docker image, amend Dockerhub README~~
* ~~Add https URLs for Twitter images~~
* ~~Sanitise dependencies~~
* Autodeploy to AWS LAMBDA using Travis only for master
* Limit Zappa IAM user and roles privileges (edit example config file)
* Make tool to analyse code performance:
`python -m cProfile -o profile_data.pyprof tests/gettwitts_tests.py`
`python -m pyprof2calltree -i profile_data.pyprof -k`
&&
https://gitlab.com/blgo/learn-more-python-the-hard-way/blob/master/ex6-find/find.py comand line arguments parser.