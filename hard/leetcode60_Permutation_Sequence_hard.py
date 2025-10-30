def getPermutation(n, k):
    #计算阶乘
    factorial=[1]*(n+1)
    for i in range(1,n+1):
        factorial[i]=factorial[i-1]*i

    #初始化数字列表
    numbers=list(range(1,n+1))
    result=[]
    k-=1

    #逐位确定数字
    for i in range(n,0,-1):
        index=k//factorial[i-1]
        result.append(str(numbers[index]))
        numbers.pop(index)
        k%=factorial[i-1]

    return ''.join(result)

print(getPermutation(7,9))

