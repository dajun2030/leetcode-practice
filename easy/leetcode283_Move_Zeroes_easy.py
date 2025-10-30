# def moveZeroes(nums):
#     slow=0
#
#     for fast in range(len(nums)):
#         if nums[fast]!=0:
#             nums[slow],nums[fast]=nums[fast],nums[slow]
#             slow+=1
#     return nums
#
# print(moveZeroes([0, 1, 0, 3, 12]))

#########################################
#方法二：先填充非零再补零
# def moveZeroes(nums):
#     slow=0
#     # 第一次遍历：将所有非零元素移到前面
#     for fast in range(len(nums)):
#         if nums[fast]!=0:
#             nums[slow]=nums[fast]
#             slow+=1
#     # 第二次遍历：将剩余位置填充为零
#     for i in range(slow,len(nums)):
#         nums[i]=0
#     return nums
#
# print(moveZeroes([0, 1, 0, 3, 12]))

############不符合题目要求#################################
from collections import deque
def moveZeroes(nums):
    queue=deque()
    for num in nums:
        if num!=0:
            queue.append(num)

    for i in range(len(nums)):
        if queue:
            nums[i]=queue.popleft()
        else:
            nums[i]=0

    return nums

print(moveZeroes([0, 1, 0, 3, 12]))