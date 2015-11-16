import re
import urllib2
from bs4 import BeautifulSoup

link = raw_input('Enter movie link: ')
name = raw_input('Name: ')
response = urllib2.urlopen(link)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all(href=re.compile('docs.google'))

for link in links:
	link2 = BeautifulSoup(link.encode('utf-8'), 'html.parser')
	print ("nohup wget '{}' -O '{}.{}..mp4' & ").format(link2.a['href'], name, link2.text.strip())
