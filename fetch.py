import re
import urllib2
from bs4 import BeautifulSoup
import sys
import os

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


def get_video_links(name, url):
	resp = urllib2.urlopen(url)
	html = resp.read()
	soup = BeautifulSoup(html, 'html.parser')
	target = soup.find('div', attrs={'class', 'filmicerik'}).findChildren('center')
	for raw in target:
		html = unicode.join(u'\n',map(unicode,raw))
		if 'docs.google' in html:
			target = raw
	target =  str(target).split('<br>')
	for raw in target:
		if 'docs.google' in raw:
			if 'Soundtrack' in raw:
				eng = raw
			else:
				th = raw
	soup = BeautifulSoup(eng, 'html.parser')
	files = []
	for link in soup.find_all(href=re.compile('docs.google')):
		link = BeautifulSoup(link.encode('utf-8'), 'html.parser')
		f = dict()
		f['name'] = name
		f['resolution'] = link.text.strip()
		f['url'] = link.a['href']
		f['lang'] = 'EN'
		files.append(f)
	soup = BeautifulSoup(th, 'html.parser')
	for link in soup.find_all(href=re.compile('docs.google')):
                link = BeautifulSoup(link.encode('utf-8'), 'html.parser')
                f = dict()
                f['name'] = name
                f['resolution'] = link.text.strip()
                f['url'] = link.a['href']
                f['lang'] = 'TH'
                files.append(f)
	return files
#	print str(target[1]).split('<br>')

get_video_links('', raw_input('Enter movie link: '))
