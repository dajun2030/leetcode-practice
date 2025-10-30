# def hammingWeight(n):
#     count=0
#     while n:
#         count+=n&1
#         n>>=1
#     return count
#
# print(hammingWeight(10))


def hammingWeight(n) :
    count = 0
    while n:
        n &= n - 1  # 清除最低位的1
        count += 1
    return count

print(hammingWeight(10))
print(bin(10))
print(hex(10))