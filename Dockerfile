FROM tiangolo/uwsgi-nginx-flask:python3.6
RUN pip install python-twitter python-env Flask-GoogleMaps
RUN rm -R /app
COPY . /app
