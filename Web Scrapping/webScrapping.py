#Webscrapping is used for writing applications that pretend to be web browsers, and retrieve the web pages.
"""
Sometimes there is no API, so we grab all the pages and pull out the data s

we use beautiful soup library 
we download it from https://www.crummy.com/software/BeautifulSoup/ and put it in the same folder as this file.
You can install Beautiful Soup 4 with pip install beautifulsoup4
"""

import urllib
from BeautifulSoup import *

url= raw_input('Enter - ' )

html= urllib.urlopen(url).read()

soup=BeautifulSoup(html)

#Now we retrieve a list of all anchor tags and each tag here is like a dictionary of HTMl attributes.

tags= soup('a')
for tag in tags:
		print tag.get('href', None)