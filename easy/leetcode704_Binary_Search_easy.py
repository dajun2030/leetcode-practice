#标准二分查找
# def search(nums, target):
#     left,right=0,len(nums)-1
#     while left<=right:
#         mid=left+(right-left)//2
#         if nums[mid]<target:
#             left=mid+1
#         elif nums[mid]>target:
#             right=mid-1
#         else:
#             return nums[mid]
#     return -1
#
# print(search(nums=[1,2,3,4,5,6,7,8,9], target=8))

# 递归实现
# class Solution:
#     def search(self, nums, target):
#         def bisearch(left, right):
#             if left > right:
#                 return -1
#
#             mid = left + (right - left) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 return bisearch(mid + 1, right)
#             else:
#                 return bisearch(left, mid - 1)
#
#         return bisearch(0, len(nums) - 1)
#
#
# solution = Solution()
# print(solution.search([1, 2, 4, 5, 8, 9, 11, 13, 15, 19, 23, 24, 43, 66, 99], 23))

#bisect模块
# import bisect
# def bisearch(nums,target):
#     index=bisect.bisect_left(nums,target)
#
#     if index<len(nums) and nums[index]==target:
#         return index
#     else:
#         return -1
#
# print(bisearch([1, 2, 4, 5, 8, 9, 11, 13, 15, 19, 23, 24, 43, 66, 99], 23))

#左开右闭
def bisearch(nums,target):
    n=len(nums)
    left=0
    right=n

    while left<right:
        mid=left+(right-left)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            right=mid
        else:
            left=mid+1
    return -1

print(bisearch([1, 2, 4, 5, 8, 9, 11, 13, 15, 19, 23, 24, 43, 66, 99], 23))