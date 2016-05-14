import xml.etree.ElementTree as ET
import urllib

url = raw_input()
data = urllib.urlopen(url).read()
tree = ET.fromstring(data)
commentInfo = tree.find('comments')
countList = commentInfo.findall('comment/count')
total = 0
for count in countList:
	total += int(count.text)

print total