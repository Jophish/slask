"""!math <mathstuffs> evaluates to mathstuffs """

from urllib import quote
import re
import requests
from random import shuffle

def math(maths):
    maths.replace("^","**")
    if maths == "2 + 2":
        return "5"
    return str(eval(maths))

def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"!math (.*)", text)
    if not match: return

    searchterm = match[0]
    return math(searchterm)
