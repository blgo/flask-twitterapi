from nose.tools import *
from twitterapi.gettwitts import *
from twitterapi.countries import countries
from twitterapi.geolocation import * 

def test_find_coordinates():
    twitts = Twitts()
    twitts.authenticate()
    twitts.get_twitts()
    assert_equal(twitts.statuses[0].lang, "en")

    assert countries.get('afghanistan', None)

    assert_equal(countries.get('afghanistan')["countrycode"], "af")
    assert_equal(countries.get('afghanistan')["lng"], 65.405957)
    assert_equal(countries.get('afghanistan')["lat"], 33.857576)

    gmarkers = GoogleMapsMarkers()
    gmarkers.find_coordinates(twitts.statuses)


if __name__ == '__main__':
    test_find_coordinates()
