from nose.tools import *
from twitterapi.gettwitts import *
from twitterapi.importcsv import *
from twitterapi.geolocation import * 

def test_find_coordinates():
    twitts = Twitts()
    twitts.authenticate()
    twitts.get_twitts()
    assert_equal(twitts.statuses[0].lang, "en")

    countries = load_countries()
    assert_equal(countries[0].name, "afghanistan")
    assert_equal(countries[0].code, "AF")
    assert_equal(countries[0].lng, 65.405957)
    assert_equal(countries[0].lat, 33.857576)

    gmarkers = GoogleMapsMarkers()
    gmarkers.find_coordinates(twitts.statuses, countries)
