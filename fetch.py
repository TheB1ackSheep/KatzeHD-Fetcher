import re
import urllib2
from bs4 import BeautifulSoup

'''link = raw_input('Enter movie link: ')
name = raw_input('Name: ')
response = urllib2.urlopen(link)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all(href=re.compile('docs.google'))

for link in links:
	link2 = BeautifulSoup(link.encode('utf-8'), 'html.parser')
	print ("nohup wget '{}' -O '{}.{}..mp4' & ").format(link2.a['href'], name, link2.text.strip())'''

def check_resume_supported(url):
	req = urllib2.Request(url)
	req.add_header('Range', 'bytes=0-1')
	resp = urllib2.urlopen(req)
	return resp.info().dict['content-length'] == '2'

