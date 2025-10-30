#方法二:数字完全翻转解法
# def isPalindrome(x):
#     if x<0:
#         return False
#
#     original=x
#     result=0
#     while x!=0:
#         digit=x%10
#         result=result*10+digit
#         x = x // 10
#
#     if result==original:
#         return True
#     else:
#         return False

#方法一：字符串解法
# def isPalindrome(x):
#     if x<0:
#         return False
#
#     s=str(x)
#     return s==s[::-1]
# print(isPalindrome(1234321))

#方法三:数字翻转一半解法
def isPalindrome(x):
    if x<0 or(x%10==0 and x!=0):
        return False
    reversed_half=0

    while x>reversed_half:
        digit=x%10
        reversed_half=reversed_half*10+digit
        x=x//10
    return x==reversed_half or x==reversed_half//10

print(isPalindrome(1234321))