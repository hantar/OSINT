from twython import Twython, TwythonStreamer, TwythonError

APP_KEY = '9juR7PXHYthviQ88fjljIP8Y3'
APP_SECRET = 'mQfK6vtSKIQqwuAFwtyEtoFBkke1FNvas0uRyUksVZn7OONVxR'
OAUTH_TOKEN = '1122520627645157376-qFVfLO9cVSc53UzEB3wEDni1P1fPJH'
OAUTH_SECRET = 'WPqT6wrUrmc3tczqvtV6cGnxgqF4zLgyph54wkmLe4GJv'

def getAccessToken(APP_KEY, APP_SECRET):
    #keys from twitter app
    APP_KEY = APP_KEY
    APP_SECRET = APP_SECRET
    #create twitter object
    twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
    ACCESS_TOKEN = twitter.obtain_access_token()
    #return access token
    return ACCESS_TOKEN

def useAccessToken(ACCESS_TOKEN):
    APP_KEY = '9juR7PXHYthviQ88fjljIP8Y3'
    ACCESS_TOKEN = ACCESS_TOKEN
    twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
    return twitter

ACCESS_TOKEN = getAccessToken(APP_KEY, APP_SECRET)

twitter = useAccessToken(ACCESS_TOKEN)

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print(data)
    def on_error(self, status_code, data):
        print(status_code, data)


