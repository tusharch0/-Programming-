def count3(nums):
    count = 0
    for num in nums:
        if num == 3:
            count = count +1

    return count 
print(count3([1,2,3,4,3,3,3]))