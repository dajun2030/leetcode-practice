# def plusOne(digits):
#     n=len(digits)
#     num=0
#     for i in range(n):
#         num+=digits[i]*10**(n-i-1)
#
#     new_num=num+1
#     m=len(str(new_num))
#     li=[]
#     count=0
#     for i in range(m):
#         new_digits=(new_num//10**(m-i-1))%10
#         li.append(new_digits)
#
#     return ''.join(map(str,li))


def plusOne(digits):
    n=len(digits)

    for i in range(n-1,-1,-1):
        if digits[i]<9:
            digits[i]+=1
            return digits
        else:
            digits[i]=0

    return [1]+digits
print(plusOne([4,3,2,9]))
print(plusOne([9,9,9,9]))