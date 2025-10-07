def minSubArrayLen(target, nums):
    left=0
    min_length=float('inf')
    current_sum=0

    for right in range(len(nums)):
        current_sum+=nums[right]

        while current_sum>=target:
            min_length=min(min_length,right-left+1)
            current_sum-=nums[left]
            left+=1

    return min_length if min_length!=float('inf') else 0


test_cases = [
    ([2,3,1,2,4,3], 7),    # 输出: 2 ([4,3])
    ([1,4,4], 4),          # 输出: 1 ([4])
    ([1,1,1,1,1,1,1,1], 11), # 输出: 0
    ([], 1),               # 输出: 0
    ([1,2,3,4,5], 15),     # 输出: 5 ([1,2,3,4,5])
]

for nums, target in test_cases:
    result = minSubArrayLen(target, nums)
    print(f"nums={nums}, target={target} -> {result}")