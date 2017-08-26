import twitter
import dotenv

dotenv.load()

api = twitter.Api(consumer_key=dotenv.get('consumer_key'),
               consumer_secret=dotenv.get('consumer_secret'),
               access_token_key=dotenv.get('access_token_key'),
               access_token_secret=dotenv.get('access_token_secret')
               )

twitteruser = dotenv.get('twitteruser')
statuses = api.GetUserTimeline(screen_name=twitteruser, count=10)
i = 0
for status in statuses:
    i += 1
    print(i,"*"*79)
    status.id_str
    print(status.created_at)
    print(status.text)
    print(status.id_str)
    print(status.coordinates)
    print(status.place)
    if status.urls:
        print(status.urls[0].url)
    for hashtag in status.hashtags:
        print(hashtag.text)
    