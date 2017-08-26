from nose.tools import *

from twitterapi.gettwitts import *

def test_get_twitts():
    '''
    Test authentication and a twitt assuming that they are always in english
    '''
    twit = Twitts()
    twit.authenticate()
    twit.get_twitts()
    assert_equal(twit.statuses[0].lang, "en")
