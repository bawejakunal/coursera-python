import urllib
from bs4 import BeautifulSoup
import re

url = raw_input('Enter URL: ')
count = int(raw_input('Enter count: '))
position = int(raw_input('Enter position: '))

while count > 0:
	soup = BeautifulSoup(urllib.urlopen(url),'lxml')
	url = soup('a')[position-1].get('href',None)
	count =  count -1

print re.search('_([a-zA-Z0-9]+)\.',url).group(1)