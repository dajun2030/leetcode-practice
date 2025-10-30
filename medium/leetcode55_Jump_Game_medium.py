#贪心算法
# def canJump(nums):
#     max_reach=0
#
#     for i in range(len(nums)):
#         if i>max_reach:
#             return False
#
#         max_reach=max(max_reach,i+nums[i])
#
#         if max_reach>=len(nums)-1:
#             return True
#     return False
#
# print(canJump([2,3,1,1,4]))
# print(canJump([2,2,1,0,4]))
# print(canJump([3,2,1,0,4]))

#动态规划法
def canJump(nums):
    n=len(nums)
    dp=[False]*n
    dp[0]=True

    for i in range(1,n):
        for j in range(i):
            if dp[j] and j+nums[j]>i:
                dp[i]=True
                break
    return dp[n-1]
