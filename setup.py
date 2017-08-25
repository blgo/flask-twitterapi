try: 
    from setptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Tweet collecting and visualisation app',
    'author': 'Blas Gomez',
    'url': 'https://github.com/blgo/flask-twitterapi',
    'author_email': 'jblas1989@gmail.com',
    'version': '0.1',
    'install_requires': ['nose, flask, python-twitter, python-env'],
    'packages': ['twitterapi'],
    'scripts': ["main.py"],
    'name': 'twitterapi'
}

setup(**config)
