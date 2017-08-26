from nose.tools import *

from twitterapi.importcsv import *

def test_create_coutries_list():
    countries = load_countries()
    assert_equal(countries[0].name,"afghanistan")
    assert_equal(countries[0].code,"AF")
    assert_equal(countries[0].lng,65.405957)
    assert_equal(countries[0].lat,33.857576)
