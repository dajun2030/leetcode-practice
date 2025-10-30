#动态规划方法
# def climbStairs(n):
#     if n<=2:
#         return n
#
#     dp=[0]*(n+1)
#     dp[1]=1
#     dp[2]=2
#
#     for i in range(3,n+1):
#         dp[i]=dp[i-1]+dp[i-2]
#
#     return dp[n]
#
# print(climbStairs(100))

#空间优化方法
def climbStairs(n):
    if n<=2:
        return n

    step2,step1=2,1
    for i in range(3,n+1):
        step1,step2=step2,step2+step1
    return step2
print(climbStairs(100))