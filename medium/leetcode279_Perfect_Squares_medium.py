def numSquares(n):
    dp=[float('inf')]*(n+1)
    dp[0]=0
    max_square=int(n**0.5)
    squares=[i*i for i in range(1,max_square+1)]

    for i in range(1,n+1):
        for square in squares:
            if i<square:
                break
            dp[i]=min(dp[i],dp[i-square]+1)
    return dp[n]

print(numSquares(12))
print(numSquares(6))
