import twitter
import os

class Twitts(object):

    def __init__ (self):
        self.api = None
        self.statuses = None

    def authenticate(self):
        self.api = twitter.Api(consumer_key=os.getenv('consumer_key'),
                    consumer_secret=os.getenv('consumer_secret'),
                    access_token_key=os.getenv('access_token_key'),
                    access_token_secret=os.getenv('access_token_secret')
                    )

    def get_twitts(self):
        twitteruser = os.getenv('twitteruser')
        self.statuses = self.api.GetUserTimeline(screen_name=twitteruser, count=10)
