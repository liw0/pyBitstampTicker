import requests, json
from datetime import datetime


r = requests.get("https://www.bitstamp.net/api/ticker")
t = json.loads(r.content)
high = t["high"]
last = t["last"]
low  = t["low"]

timestamp = datetime.now().strftime('%b %d %H:%M:%S')

print timestamp
print "high:", high
print "low:", low
print "last:", last
