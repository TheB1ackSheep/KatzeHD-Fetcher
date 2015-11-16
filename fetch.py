import re
import urllib2
from bs4 import BeautifulSoup
import sys
import os
import subprocess

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
		f['file_name'] = name + '.EN.'  + f['resolution'] + '.mp4'
		files.append(f)
	soup = BeautifulSoup(th, 'html.parser')
	for link in soup.find_all(href=re.compile('docs.google')):
                link = BeautifulSoup(link.encode('utf-8'), 'html.parser')
                f = dict()
                f['name'] = name
                f['resolution'] = link.text.strip()
                f['url'] = link.a['href']
                f['lang'] = 'TH'
		f['file_name'] = name + '.TH.'  + f['resolution'] + '.mp4'
                files.append(f)
	return files

def download_videos(name, videos):
	real_dir = os.path.join(os.getcwd(), name)+os.sep
	if not os.path.isdir(os.getcwd()+name):
		os.mkdir(real_dir)
	for video in videos:
		subprocess.Popen(["nohup", "wget", video['url'], "-O", real_dir+video['file_name']])


name = raw_input('Enter Movie Name: ').replace(' ','.')
url = raw_input('Enter movie link: ')
videos = get_video_links(name,url)
print "Movie url fetched. Start downloading..."
download_videos(name, videos)
print "Downloading is running in background. Done !!!"
