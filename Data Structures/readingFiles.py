# Use words.txt as the file name

"""
a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. 
The file words.txt to produce the output below is used
You can download the sample data at http://www.pythonlearn.com/code/words.txt

"""
fname = raw_input("Enter file name: ")

fh= open(fname)

for i in fh:
	i= i.rstrip().upper()
	print i
	