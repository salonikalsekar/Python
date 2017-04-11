# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *


url = raw_input('Enter - ')

def 
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('a')

print tags[2].get('href', None)


i=1
while (i<4):
	
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
