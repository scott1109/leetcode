def twoSum(nums,target):
    for i in range(len(nums)):
        if target - nums[i] in nums[i+1:]:
            return [i,nums[i+1:].index(target - nums[i])+i+1]
#要注意索引的值，因为你如果从i后面一位开始索引，那么真正的索引是针对原数列的，那么我们就需要加上i+1，也就是要加上这一个
#数列的第一个数的index在原数列的index值，才是真正的值
优化：建立了一个空的字典，以原本的value作为key，然后索引作为值
lookup = {}
for i,num in enumerate(nums):
    if target - num in lookup:
        return [lookup[target - num],i]
    lookup[num] = i
# test
a =0
return 0