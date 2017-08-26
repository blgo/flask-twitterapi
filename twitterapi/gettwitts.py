import twitter
import dotenv

class Twitts(object):

    def __init__ (self):
        dotenv.load()
        self.api = None
        self.statuses = None

    def authenticate(self):
        self.api = twitter.Api(consumer_key=dotenv.get('consumer_key'),
                    consumer_secret=dotenv.get('consumer_secret'),
                    access_token_key=dotenv.get('access_token_key'),
                    access_token_secret=dotenv.get('access_token_secret')
                    )

    def get_twitts(self):
        twitteruser = dotenv.get('twitteruser')
        self.statuses = self.api.GetUserTimeline(screen_name=twitteruser, count=10)
