"""!math <mathstuffs> evaluates to mathstuffs """

# joe bergeron

from urllib import quote
import re
import requests
from random import shuffle

def math(maths):
    maths = maths.replace("^","**")
    math2 = maths
    math2 = math2.replace(" ", "")
    if math2 == "2+2":
        return "5"
    return str(eval(maths))

def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"!math (.*)", text)
    if not match: return

    searchterm = match[0]
    return math(searchterm)
