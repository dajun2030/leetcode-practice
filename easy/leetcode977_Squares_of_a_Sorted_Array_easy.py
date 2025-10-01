#思路1：直接平方 + 排序（暴力法）
# def sortedSquares(nums):
#     li=[]
#     for num in nums:
#         li.append(abs(num)**2)
#     return sorted(li)

#双指针法
def sortedSquares(nums):
    n=len(nums)
    left,right=0,n-1
    pos=n-1
    result=[0]*n

    while left<=right:
        left_square=nums[left]**2
        right_square=nums[right]**2
        if left_square>right_square:
            result[pos]=left_square
            left+=1
        else:
            result[pos]=right_square
            right-=1
        pos-=1

    return result
print(sortedSquares([-4,-1,0,3,10]))