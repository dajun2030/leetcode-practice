# def majorityElement(nums):
#     from collections import Counter
#     maj=Counter(nums)
#     n=len(nums)
#     for num,count in maj.items():
#         if count>n/2:
#             return num
#     return -1


#哈希表计数
# def majorityElement(nums):
#     count_map={}
#     for num in nums:
#         if num in count_map:
#             count_map[num]+=1
#         else:
#             count_map[num]=1
#     n=len(nums)
#     for num,count in count_map.items():
#         if count>n/2:
#             return num
#     return -1

# def majorityElement(nums):
#     # 对数组进行排序
#     nums.sort()
#
#     # 由于众数出现次数超过一半，中间位置的元素一定是众数
#     return nums[len(nums) // 2]

#Boyer-Moore投票算法
def majorityElement(nums):
    candidate=None
    count=0

    for num in nums:
        if count==0:
            candidate=num
            if num==candidate:
                count+=1
            else:
                count-=1
    return candidate
print(majorityElement([2,2,1,1,1,2,2]))

