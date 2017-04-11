

"""
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""
def openFile():
    fname = raw_input("Enter file name: ")
    if len(fname) < 1 : fname = "mbox-short.txt"
    try:
        fh = open(fname, 'r')
    except:
        print "Error opening file", fname
        quit()
    return fh
	
def counting(lines,s):
    c = dict()
    for line in lines:
        if line.startswith(s) and not line.startswith(s+':'):
            line = ((line.rstrip()).lstrip()).split()
	    str = line[5]
	    hour = str[0:str.find(":"):1]
            c[hour] = c.get(hour,0) + 1
    return c

def startsWith():
    sw = raw_input("Enter line prefix to consider: ")
    if len(sw) < 1 : sw = "From"
    return sw



def sorting(d):
    lst = list()
    for key, val in d.items():
        lst.append((key,val))
    lst.sort()
    for val,key in lst:
        print val,key
    
fh = openFile()
sw = startsWith()
dictionary = counting(fh,sw)
t = sorting(dictionary)