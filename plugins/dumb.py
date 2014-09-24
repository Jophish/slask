"""!why are you so dumb"""

# joe bergeron

from urllib import quote
import re
import requests
import random

def dumb():
    responses = ["i'm so sorry", "i don't know"]

    return random.choice(responses)

def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"!math (.*)", text)
    if not match: return

    searchterm = match[0]
    if searchterm.replace(" ", "") == "areyousodumb":
        return dumb()
    else:
        return
