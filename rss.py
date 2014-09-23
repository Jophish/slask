import feedparser
import requests
import json
import time
import bs4
import feeds

link = "https://shfriends.slack.com/services/hooks/incoming-webhook?token=IaEYnLmPQCYxdoQypHnK52Al"

links = feeds.links
usernames = feeds.usernames
icons = feeds.icons

currentArticles = [None]*len(links)
recentArticles = [None]*len(links)

check = False #enable if you don't want the bot spamming the channel with rss feeds when it's turned on

while True:

	for x in list(range(len(links))):

		d = feedparser.parse(links[x])
		currentArticles[x] = d['entries'][0]['title']

		if str(recentArticles[x]) != str(currentArticles[x]):

			recentArticles[x] = str(d['entries'][0]['title'])		
			session = requests.session()
			req = session.get('http://tinyurl.com/api-create.php?url='+d['entries'][0]['link'])
			doc =  str(bs4.BeautifulSoup(req.content)) #[15:-18]
			print(doc)
			payload = json.JSONEncoder().encode({"username": usernames[x], "icon_url" : icons[x], "attachments" : [{"title": d['entries'][0]['title'], "text": '\n'+d['entries'][0]['summary_detail']['value'][:d['entries'][0]['summary_detail']['value'].index('<')] +'\n' + str(doc)}]})

			if check == True:
				check = False
			else: 
				requests.post(link, payload)



		time.sleep(1)

