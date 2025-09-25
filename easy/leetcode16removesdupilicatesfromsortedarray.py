#双指针法
# def removeDuplicates(nums) :
#     slow=0
#     for fast in range(1, len(nums)):
#         if nums[slow]!=nums[fast]:
#             slow+=1
#             nums[slow]=nums[fast]
#     return slow+1

#计数覆盖法
# 核心思路
# 与双指针法类似，但更直观：显式记录当前唯一元素的值，当遇到不同值时才进行覆盖。

def removeDuplicates(nums) :
    if not nums:
        return 0
    current=nums[0]
    count=1
    for i in range(1,len(nums)):
        if nums[i]!=current:
            nums[count]=nums[i]
            count+=1
            current=nums[i]
    return count


print(removeDuplicates([0,0,1,1,1,2,2,3,3,4,4,55,6,7,8,8,8,8,8,9]))