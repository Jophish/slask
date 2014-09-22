"""!dorito returns a dorito """

# joe bergeron

from urllib import quote
import re
import requests



def on_message(msg, server):

    link = "http://tinyurl.com/n4a4l6m"

    text = msg.get("text", "")
    match = re.findall(r"!dorito", text)
    if not match: return

    searchterm = match[0]
    return link
