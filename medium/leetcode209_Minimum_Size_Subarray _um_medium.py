# def minSubArrayLen(target, nums):
#     left=0
#     min_length=float('inf')
#     current_sum=0
#
#     for right in range(len(nums)):
#         current_sum+=nums[right]
#
#         while current_sum>=target:
#             min_length=min(min_length,right-left+1)
#             current_sum-=nums[left]
#             left+=1
#
#     return min_length if min_length!=float('inf') else 0
#
#
# test_cases = [
#     ([2,3,1,2,4,3], 7),    # 输出: 2 ([4,3])
#     ([1,4,4], 4),          # 输出: 1 ([4])
#     ([1,1,1,1,1,1,1,1], 11), # 输出: 0
#     ([], 1),               # 输出: 0
#     ([1,2,3,4,5], 15),     # 输出: 5 ([1,2,3,4,5])
# ]
#
# for nums, target in test_cases:
#     result = minSubArrayLen(target, nums)
#     print(f"nums={nums}, target={target} -> {result}")

#前缀和+二分查找
def minSubArrayLen(target, nums):
    if not nums:
        return 0

    n=len(nums)
    prefix=[0]*(n+1)
    for i in range(1,n+1):
        prefix[i]=prefix[i-1]+nums[i-1]

    min_length=float('inf')

    for start in range(n):
        left,right=start,n
        while left<right:
            mid=left+(right-left)//2
            if prefix[mid]-prefix[start]>=target:
                right=mid
            else:
                left=mid+1

        if left<=n and prefix[left]-prefix[start]>=target:
            min_length=min(min_length, left-start)
    return min_length if min_length!=float('inf') else 0

print(minSubArrayLen(7,[2,3,1,2,4,3]))