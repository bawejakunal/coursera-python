import urllib
import json

url = raw_input('Enter json file location: ')

handle = urllib.urlopen(url)
json_data =  json.load(handle)

total = 0
for comment in json_data['comments']:
	total += comment['count']

print total