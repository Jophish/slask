"""!btc returns the 24 hour average for btc/usd"""

import BeautifulSoup as bs4
from urllib import quote
import re
import requests
from random import shuffle, randint




def btc():


    session = requests.session()
    req = session.get('https://api.bitcoinaverage.com/all')
    doc =  str(bs4.BeautifulSoup(req.content)) #[15:-18]
    doc = doc.split('USD')[1][40:46]
    return("1 btc -> " + doc + " usd")

print(btc())
def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"!btc", text)
    if not match: return

    return btc()
