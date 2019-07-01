

nums = [5,88,32,2,1,6]
min = nums[0]
def sort(nums):
    for i in range(len(nums)):
        minpos = i
        for j in range(i, len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp




sort(nums)
print(nums)