# def minCostClimbingStairs(cost):
#     n=len(cost)
#     dp=[0]*(n+1)
#
#     dp[0]=0
#     dp[1]=0
#
#     for i in range(2,n+1):
#         dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
#
#     return dp[n]
#
# print(minCostClimbingStairs( [10, 15, 20]))
# print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
#
#
def minCostClimbingStairs_min(cost):
    n = len(cost)
    if n <= 1:
        return 0
    a, b = 0, 0
    for i in range(2, n+1):
        a, b = b, min(b + cost[i-1], a + cost[i-2])
    return b

cost = [10, 15, 20]
result = minCostClimbingStairs_min(cost)
print("最小花费:", result)