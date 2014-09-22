"""!dorito returns a dorito """

# joe bergeron

from urllib import quote
import re
import requests
from random import shuffle


def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"!dorito (.*)", text)
    if not match: return

    searchterm = match[0]
    return "https://scontent-a-lga.xx.fbcdn.net/hphotos-xap1/v/t1.0-9/1489031_794808267212568_124215925_n.jpg?oh=7a29c9af17d475156581364c24984047&oe=54894CDA"
