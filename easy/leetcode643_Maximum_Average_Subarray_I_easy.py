def findMaxAverage(nums, k):
    current_sum = sum(nums[:k])
    max_sum = current_sum

    for i in range(k, len(nums)):
        current_sum = current_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, current_sum)

    return max_sum /  float(k)


# 测试用例
test_cases = [
    ([1, 12, -5, -6, 50, 3], 4),  # 输出: 12.75
    ([5], 1),  # 输出: 5.0
    ([0, 4, 0, 3, 2], 1),  # 输出: 4.0
    ([1, 2, 3, 4, 5], 3),  # 输出: 4.0
    ([-1, -2, -3, -4, -5], 3),  # 输出: -2.0
]

for nums, k in test_cases:
    result = findMaxAverage(nums, k)
    print(f"nums = {nums}, k = {k}, maxAverage = {result}")


