#Regular Expressions

# provides a meaning full and a flexible way to match and extract the string or pattern of characters

#It itself is a progamming language. 
# ^ Start of the program
#$ end of the line
#. matches any char
#\s matches whitespaces
#\S matches non-whitespaces
#* Repeats a char for zero or more times
#+ Repeats a char for one or more times
#*? Repeats a char for zero or more times(non-greedy)
#+? Repeats a char for one or more times(non-greedy)
#( Where to start extraction 
#) Where to end extraction

#re.search() works as find()

#Wild card char is . 

#importing to regular expression library 

# parathesis tell what to extraction

#x= 'From salonikalsekar1@gmail.com Sat April 8

#y= re.findall(' ^From (\S+@\S+)',x)
#print y 
['salonikalsekar1@gmail.com']
 
import re 

##x= "From: Using : char: hi"
##y= re.findall('^F.+:',x)
#print y

file= open("a.txt").read()
y= re.findall('[0-9]+',file)
sum=0
for num in y :
	num=int(num)
	sum=sum+ num 
print sum 
	
