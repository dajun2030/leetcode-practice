#方法一：快慢指针（保持顺序）
# def removeElement(nums, val):
#     slow=0
#
#     for fast in range(len(nums)):
#         if nums[fast]!=val:
#             nums[slow]=nums[fast]
#             slow+=1
#     return slow
#
# print(removeElement([3, 2, 2, 3],3))

#方法二：首尾指针（不保持顺序，更高效）
def removeElement(nums, val):
    left,right=0,len(nums)-1
    while left<=right:
        if nums[left]==val:
            nums[left]=nums[right]
            right-=1
        else:
            left+=1
    return left
print(removeElement([3, 2, 2, 3],3))


