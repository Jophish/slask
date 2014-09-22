import feedparser
import requests
import json
import time
import bs4

d = feedparser.parse('http://rss.nytimes.com/services/xml/rss/nyt/World.xml')


link = "https://shfriends.slack.com/services/hooks/incoming-webhook?token=IaEYnLmPQCYxdoQypHnK52Al"



recentArticle = None

while True:

	d = feedparser.parse('http://rss.nytimes.com/services/xml/rss/nyt/World.xml')

	if recentArticle != d['entries'][0]['title']:

		recentArticle = d['entries'][0]['title']
		
		session = requests.session()

		req = session.get('http://tinyurl.com/api-create.php?url='+d['entries'][0]['link'])

		doc =  str(bs4.BeautifulSoup(req.content)) #[15:-18]


		payload = json.JSONEncoder().encode({"username": "NY Times", "icon_url" : "http://ryanmartin.me/wp-content/uploads/2014/05/Elkhart-Truth-new-website-favicon.png", "attachments" : [{"title": d['entries'][0]['title'], "text": d['entries'][0]['published'] + "\n "+ str(doc)}, ]})

		r = requests.post(link, payload)

		time.sleep(30)


	time.sleep(1)



def rss():

	pass


def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"!rss", text)
    if not match: return

    return rss()