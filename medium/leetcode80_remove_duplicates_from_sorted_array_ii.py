#通用模版法：双指针
# def removeDuplicates(nums) -> int:
#     if len(nums)<=2:
#         return len(nums)
#     k = 2
#
#     for i in range(2,len(nums)):
#         if nums[i] != nums[k-2]:
#             nums[k] = nums[i]
#             k += 1
#     return k


def removeDuplicates(nums):
    if len(nums) <= 2:
        return len(nums)

    k = 1
    count = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            count += 1
        else:
            count = 1

        if count <= 2:
            nums[k] = nums[i]
            k += 1

    return k
print(removeDuplicates([1, 1, 1, 2, 2, 3]))