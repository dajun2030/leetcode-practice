# #暴力枚举法
# def lenLongestFibSubseq(A):
#     s=set(A)
#     n=len(s)
#     result=0
#
#     for i in range(n):
#         for j in range(i+1,n):
#             a,b=A[i],A[j]
#             count=2
#             while a+b in s:
#                 a,b=b,a+b
#                 count+=1
#             result=max(result,count)
#     return result if result>2 else 0

#动态规划法
def lenLongestFibSubseq(arr):
    n=len(arr)
    index_map={x:i for i,x in enumerate(arr)}

    dp=[[2]*n for _ in range(n)]
    max_len=0

    for j in range(n):
        for i in range(j):
            prev=arr[j]-arr[i]
            if prev in index_map and prev<arr[i]:
                k=index_map[prev]
                dp[i][j]=dp[k][i]+1
                max_len=max(max_len,dp[i][j])
    return max_len if max_len>=3 else 0

print(lenLongestFibSubseq([1,2,3,4,5,6,7,8,9,13,14,15]))