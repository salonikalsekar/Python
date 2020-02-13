#open the file
f = open('arrays.py', 'r')

#to read the file content
# print(f.read())

#print the contents
print(f.readline(4), end="")
print(f.readline())

f1 = open('abc', 'w')
f1.write("haha hehe lol")

f2 = open('abc', 'a')
f2.write(" cant stop laughing")


# copy from arrays to abc
for i in f:
    f2.write(i)



# copying image and creating a new image from it
i =  open('image.jpeg', 'rb')

pic = open('newimage.jpeg', 'wb')

for data in i:
    pic.write(data)
