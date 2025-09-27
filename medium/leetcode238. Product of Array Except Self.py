# def productExceptSelf(nums) :
#     n=len(nums)
#     answer=[1]*n
#
#     prefix=1
#     for i in range(n) :
#         answer[i]=prefix
#         prefix*=nums[i]
#
#     suffix=1
#     for i in range(n-1,-1,-1) :
#         answer[i]*=suffix
#         suffix*=nums[i]
#
#     return answer

#使用左右积数组
# def productExceptSelf(nums) :
#     n=len(nums)
#     left=[1]*n
#     right=[1]*n
#     answer=[1]*n
#     for i in range(1,n):
#         left[i]=left[i-1]*nums[i-1]
#
#     for i in range(n-2,-1,-1):
#         right[i]=right[i+1]*nums[i+1]
#
#     for i in range(n):
#         answer[i]=left[i]*right[i]
#     return answer

#左右数组，一次循环
def productExceptSelf(nums) :
    left_product=1
    right_product=1
    n=len(nums)
    left=[0]*n
    right=[0]*n

    for i in range(n):
        j=n-i-1
        left[i]=left_product
        right[j]=right_product
        left_product*=nums[i]
        right_product*=nums[j]

    return [l*r for l,r in zip(left,right)]

print(productExceptSelf([1,1,2,2,2]))