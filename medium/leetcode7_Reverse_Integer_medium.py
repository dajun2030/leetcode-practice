#数学解法
# def reverse(x):
#     INT_MAX=2**31-1
#     INT_MIN=-2**31
#
#     result=0
#     sign=1 if x>=0 else -1
#     x=abs(x)
#
#     while x!=0:
#         digit=x%10
#         x=x//10
#
#         if (result>INT_MAX//10 or (result==INT_MAX//10 and digit>INT_MAX%10)):
#             return 0
#         #allowed_max=INT_MAX//10
#         #last_digit_max=INT_MAX%10
#         #if result>allowed_max:
#         #   return 0
#         #elif result==allowed_max and digit>last_digit_max:
#         #   return 0
#         #
#         result=result*10+digit
#     return sign*result

#字符串解法
def reverse(x):
    INT_MAX=2**31-1
    INT_MIN=-2**31

    sign=1
    if x<0:
        sign=-1
        x=-x

    reverse_str=str(x)[::-1]
    result=sign*int(reverse_str)

    if result<INT_MIN or result>INT_MAX:
        return 0
    return result

print(reverse(123))
print(reverse(-123))
print(reverse(0))
print(reverse(1534236469))

