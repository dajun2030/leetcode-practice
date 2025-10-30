# def mySqrt(x):
#     if x==0 or x==1:
#         return x
#
#     left,right=0,x
#     while left<right:
#         mid=left+(right-left)//2
#         square=mid*mid
#         if square==x:
#             return mid
#         elif square<x:
#             left=mid+1
#         else:
#             right=mid-1
#     return right

def mySqrt(x):
    if x<2:
        return x

    left,right=1,x//2
    while left<=right:
        mid=left+(right-left)//2
        if mid>x/mid:
            right=mid-1
        else:
            left=mid+1
    return left-1

print(mySqrt(10))
print(mySqrt(100))
