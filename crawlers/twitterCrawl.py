from crawlers.twitterFunc import *
import time
from datetime import datetime
from demo.models import Datacrawl, Category

ACCESS_TOKEN = getAccessToken(APP_KEY, APP_SECRET)
twitter = useAccessToken(ACCESS_TOKEN)
stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_SECRET)

def twitterStream(keyword):
	try:
		search = twitter.cursor(twitter.search, q=keyword, result_type='mixed', count=2, return_pages=True, tweet_mode='extended')
		count = 0
		for page in search:
			for result in page:
				if count < 5:
					text = result['text'] if 'text' in result else result['full_text']
					is_retweet = True if 'retweeted_status' in result or 'quoted_status' in result else False
					user_id = result['user']['id_str']
					username = result['user']['screen_name']
					post_id = result['id_str']
					url = "https://twitter.com/{}/status/{}".format(username, post_id)
					created = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(result['created_at'], '%a %b %d %H:%M:%S +0000 %Y'))
					hashtags = [_hashtag['text'].lower() for _hashtag in result['entities']['hashtags']]

					db = Datacrawl(type_id=2, text=text, username=username, url=url, created=created)
					db.save()
					count+=1
	except Exception as e:
		print(e)