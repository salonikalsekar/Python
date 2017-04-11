#From sockets to application 
#1.  we import the socket package and create the end point
#2.  connect to the end point and send the application get request 
#3.  and then receive the data and close the socket


import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
mysocket.connect(('www.py4inf.com',80))

mysocket.send('GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n')


while True: 

	data = mysocket.recv(512)
	if (len(data)< 1):
		break
	print data 

	mysocket.close()
	
"""

#Using urllib makes use of urls as files

import urllib 

data= urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

for line in data:
	print line.strip()
	
	"""