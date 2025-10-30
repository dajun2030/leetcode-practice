#双指针法
def removeDuplicates(nums):
    if not nums:
        return 0

    slow=1
    for fast in range(1,len(nums)):
        if nums[fast]!=nums[fast-1]:
            nums[slow]=nums[fast]
            slow+=1
    print(nums)
    return slow
print(removeDuplicates([1]))

#左右指针
# def removeDuplicates(nums):
#     if not nums:
#         return 0
#
#     left,right=0,1
#     while right<len(nums):
#         if nums[left]!=nums[right]:
#             left += 1
#             nums[left]=nums[right]
#
#         right+=1
#     print(nums)
#     return left+1
#
# print(removeDuplicates([1,1,2,2,2,3,3,3,4,5,6]))