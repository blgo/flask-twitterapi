from nose.tools import *

from twitterapi.importcsv import *

def test_create_coutries_list():
    countries = load_countries()
    assert_equal(countries[0].name,"afghanistan")
