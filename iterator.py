nums = [3,4,5,6,7,8]

# for i in nums:
#     print(i)


# print(iter(nums).__next__())
# print(next(iter(nums)))

# stop the loop by raising exception- raise stopIteration

# generators will give iterators
# we use yield here
def topten():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5



values = topten()
print(values.__next__())
print(values.__next__())

for i in values:
    print(i)