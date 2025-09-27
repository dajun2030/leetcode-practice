# def sortColors(nums) :
#     low,mid,high=0,0,len(nums)-1
#     while mid<=high:
#         if nums[mid]==0:
#             nums[mid],nums[low]=nums[low],nums[mid]
#             low+=1
#             mid+=1
#         elif nums[mid]==1:
#             mid+=1
#         else:
#             nums[mid],nums[high]=nums[high],nums[mid]
#             high-=1
#     return nums

#三色排序 + 计数填充
def sortColors(nums):
    counts=[0,0,0]
    for num in nums:
        counts[num]+=1
    R,W,B=counts
    nums[:R]=[0]*R
    nums[R:R+W]=[1]*W
    nums[R+W:]=[2]*B
    return nums

print(sortColors([2, 0, 2, 1, 1, 0]))








