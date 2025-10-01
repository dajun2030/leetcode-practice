#暴力枚举法
# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i]+nums[j] ==target:
#                 return [i,j]
#     return None

#哈希表
# def twoSum(nums, target):
#     num_map={}
#     for i,num in enumerate(nums):
#         complement=target-num
#         if complement in num_map:
#             return [num_map[complement],i]
#         num_map[num] = i
#     return []

#两次遍历哈希表
def twoSum(nums, target):
    nums_map={}
    for i,num in enumerate(nums):
        nums_map[num]=i

    for i,num in enumerate(nums):
        complement=target-num
        if complement in nums_map and nums_map[complement]!=i:
            return [i,nums_map[complement]]
    return []
print(twoSum(([2,7,11,15]),9))