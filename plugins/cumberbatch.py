"""!cumberbatch returns some permutation of the related actor"""

# joe bergeron

from urllib import quote
import re
import requests
import random

def cumberbatch():
	firsthalf = ['bene', 'bloople','doodle','blonkle','ziggle','doople', 'penis', 'blop','bum','butt','zongle','fingle','flopple','flop','fuzzy','fungus']
	firstend = ['flop','dict','pop','blop','blorp','flop','cum','dick','florp','pants','fuggle', 'dorp']

	secondhalf = ['cumber','frazzle','dizzle','bloopy','bloppy','fuggle','flippity','cucumber','fizzle','corona','quizzle', 'kumquat','apple','corn']
	secondend = ['flub','pants', 'florp', 'bumble', 'butt','bingle','fluff','dumpster', 'nozzle', 'tomato', 'cornhole', 'cat', 'hair', 'blunt']

	return (random.choice(firsthalf)+random.choice(firstend)+' '+random.choice(secondhalf)+random.choice(secondend))


def on_message(msg, server):



    text = msg.get("text", "")
    match = re.findall(r"!cumberbatch", text)
    if not match: return

    searchterm = match[0]
    return cumberbatch()
