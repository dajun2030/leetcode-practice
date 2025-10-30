#集合长度
# def containsDuplicate(nums):
#     length=len(nums)
#     nums_set=set(nums)
#     length_set=len(nums_set)
#     if length!=length_set:
#         return True
#     else:
#         return False
#
# print(containsDuplicate([1,2,3,3]))

#排序法
# def containsDuplicate(nums):
#     nums.sort()
#     for i in range(1,len(nums)):
#         if nums[i]==nums[i-1]:
#             return True
#     return False
#
# print(containsDuplicate([1,2,3,3]))

#哈希集的方法
def containsDuplicate(nums):
    seen=set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

print(containsDuplicate([1,2,3,3]))