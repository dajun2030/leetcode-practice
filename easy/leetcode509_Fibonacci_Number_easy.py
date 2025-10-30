 #递归法 暴力 n不能太大
# class Solution:
#     def fib(self, n: int) -> int:
#         if n <= 1:
#             return n
#         return self.fib(n-1) + self.fib(n-2)
##############################################

# def fib(n):
#     if n<=1:
#         return n
#     a,b=0,1
#     for _ in range(2,n+1):
#         a,b=b,a+b
#     return b
#
# print(fib(100))

############################################
#动态规划版本
def fib(n):
    if n<=1:
        return n

    dp=[0]*(n+1)
    dp[0]=0
    dp[1]=1

    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]

print(fib(100))