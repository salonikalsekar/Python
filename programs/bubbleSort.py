

nums = [5,88,32,2,1,6]

def sort(nums):
    for i in range(len(nums)-1, 0 , -1):
        for j in range(0, i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp




sort(nums)
print(nums)