import praw
from datetime import datetime
from demo.models import Datacrawl, Category

# Create an app: https://www.reddit.com/prefs/apps
# Use http://localhost:8000 as redirect uri
username = "IITOSINT"
password = "cyberSecurity#3"
clientid = "-Rad9IAHKYUTdQ"
clientsecret = "EqE06aQr0RLdAW2LS2WZ8Azo7pk"

reddit = praw.Reddit(client_id=clientid,
                     client_secret=clientsecret,
                     password=password,
                     user_agent='Reddit search data extractor by /u/' + username + '',
                     username=username)

def crawlReddit(keyword):
	try:
		search = keyword
		search_list = search.split(',')
		for search in search_list:
			count = 0
			for submission in reddit.subreddit('all').search(search.lower(), sort='hot'):
				if count < 5:
					db = Datacrawl(type_id=3,text=submission.title,username=submission.author,url=submission.url,
					               created=datetime.utcfromtimestamp(submission.created).strftime('%Y-%m-%d %H:%M:%S'))
					db.save()
					count+=1
	except Exception as e:
		print(e)
