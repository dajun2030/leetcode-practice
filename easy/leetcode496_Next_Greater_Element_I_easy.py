# def nextGreaterElement(nums1, nums2):
#     #用字典记录nums2的每一个元素的下一个更大元素
#     next_greater={}
#     stack=[]     #单调递减栈
#
#     #遍历nums2中每一个元素，找到每个元素的下一个更大元素
#     for num in nums2:
#         #当栈不为空，且当前元素大于栈顶元素时
#         while stack and num>stack[-1]:
#             #栈顶元素的下一个更大元素就是当前元素
#             next_greater[stack.pop()]=num
#         #当前元素入栈
#         stack.append(num)
#
#     # 栈中剩余元素没有下一个更大元素，设为 -1
#     while stack:
#         next_greater[stack.pop()]=-1
#
#     # 返回 nums1 中对应元素的结果
#     return [next_greater[num] for num in nums1]
#
# print(nextGreaterElement([4, 1,2], [1, 3, 4, 2]))

#双栈法
def nextGreaterElement(nums1, nums2):
    result=[] # 存储最终结果
    stack=[] # 主栈，用于存储nums2的所有元素

    for num in nums2:
        stack.append(num)

    for num in nums1:# 对于 nums1 中的每个元素
        temp_stack=[] # 临时栈，用于保存弹出的元素
        isFound=False# 标记是否找到了目标元素
        max=-1  # 存储下一个更大元素，初始为-1

        while stack and not isFound:
            top=stack.pop()# 弹出栈顶元素
            if top>num:
                max=top # 如果当前元素比目标大，更新max
            elif top==num:
                isFound=True# 找到目标元素，停止搜索
            temp_stack.append(top) # 将弹出的元素保存到临时栈
        result.append(max)

        #将临时栈中的元素按原顺序压回主栈
        while temp_stack:
            stack.append(temp_stack.pop())
    return result# 将结果加入结果列表

print(nextGreaterElement([4, 1,2], [1, 3, 4, 2]))