from twython import Twython
# https://github.com/ryanmcgrath/twython

APP_KEY = ''  # insert app key here
APP_SECRET = ''  # insert app secret here

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

x = twitter.search(q='#cowboys', lang='en')

for status in x['statuses']:
    print('************')
    print(status['text'])