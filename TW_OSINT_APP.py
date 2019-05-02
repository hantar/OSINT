from twython import Twython, TwythonError, TwythonStreamer
import json
import TW_OSINT_FUNCTIONS

#get an OAUTH2 access token
ACCESS_TOKEN = TW_OSINT_FUNCTIONS.getAccessToken(TW_OSINT_FUNCTIONS.APP_KEY, TW_OSINT_FUNCTIONS.APP_SECRET)

#authenticate and create twitter object
twitter = TW_OSINT_FUNCTIONS.useAccessToken(ACCESS_TOKEN)

#create streamer object
stream = TW_OSINT_FUNCTIONS.MyStreamer(TW_OSINT_FUNCTIONS.APP_KEY, TW_OSINT_FUNCTIONS.APP_SECRET, TW_OSINT_FUNCTIONS.OAUTH_TOKEN, TW_OSINT_FUNCTIONS.OAUTH_SECRET)

#get user search term 
search_term = input("Enter a search term: ")

print(stream.statuses.filter(track=search_term))

