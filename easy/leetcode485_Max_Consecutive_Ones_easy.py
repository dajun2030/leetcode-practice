# def findMaxConsecutiveOnes(nums):
#     current_count=0
#     max_count=0
#
#     for i in range(0,len(nums)):
#         if nums[i]==1:
#             current_count+=1
#             max_count=max(max_count,current_count)
#         else:
#             current_count=0
#     return max_count
#
# print(findMaxConsecutiveOnes([1,0,1,1,0,1,1,1,0,1,1,1,1]))
####################################################################################

# def findMaxConsecutiveOnes(nums):
#     return max(map(len,''.join(map(str,nums)).split('0')))
#
# print(findMaxConsecutiveOnes([1,0,1,1,0,1,1,1,0,1,1,1,1]))

###############################################################################
#双指针法
def findMaxConsecutiveOnes(nums):
    left=0
    max_count=0

    for right in range(len(nums)):
        if nums[right]==0:
            left=right+1
        current_length=right-left+1
        max_count=max(max_count,current_length)
    return max_count

print(findMaxConsecutiveOnes([1,0,1,1,0,1,1,1,0,1,1,1,1]))
