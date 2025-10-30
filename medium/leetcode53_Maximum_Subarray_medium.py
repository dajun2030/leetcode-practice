# def maxSubArray(nums):
#     n=len(nums)
#     dp=[0]*n
#     dp[0]=nums[0]
#
#     for i in range(1,n):
#         dp[i]=max(nums[i],dp[i-1]+nums[i])
#     print(dp)
#     return max(dp)
#
# print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


# def maxSubArray(nums):
#     """
#     最大子数组和问题的Python Tutor版本
#     """
#     print(f"输入数组: {nums}")
#     print(f"数组长度: {len(nums)}")
#     print("目标: 找到和最大的连续子数组")
#     print()
#
#     if not nums:
#         return
#
#     max_sum = nums[0]  # 全局最大和
#     current_sum = nums[0]  # 当前子数组和
#
#     print(f"初始化:")
#     print(f"  max_sum = nums[0] = {max_sum}")
#     print(f"  current_sum = nums[0] = {current_sum}")
#     print()
#
#     for i in range(1, len(nums)):
#         print(f"处理第{i}个元素: nums[{i}] = {nums[i]}")
#
#         # 决策：是单独开始新的子数组，还是扩展当前的子数组
#         option1 = nums[i]  # 单独开始新的子数组
#         option2 = current_sum + nums[i]  # 扩展当前子数组
#         current_sum = max(option1, option2)
#
#         print(f"  选择1: 单独开始新子数组 = {option1}")
#         print(f"  选择2: 扩展当前子数组 = {option2}")
#         print(f"  当前子数组和更新为: max({option1}, {option2}) = {current_sum}")
#
#         # 更新全局最大值
#         old_max = max_sum
#         max_sum = max(max_sum, current_sum)
#
#         print(f"  全局最大值: max({old_max}, {current_sum}) = {max_sum}")
#         print()
#
#     print(f"🎯 最大子数组和: {max_sum}")
#     return max_sum
#
#
# # 测试
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# result = maxSubArray(nums)

#分治法
class Solution:
    def maxSubArray(self, nums):
        """
        分治法求解最大子数组和
        """
        def max_crossing_sum(left,mid,right):
            left_sum=float('-inf')
            current_sum=0
            for i in range(mid,left-1,-1):
                current_sum+=nums[i]
                left_sum=max(left_sum,current_sum)

            right_sum=float('-inf')
            current_sum=0
            for i in range(mid+1,right+1):
                current_sum+=nums[i]
                right_sum=max(right_sum,current_sum)

            return left_sum+right_sum

        def max_subarray_rec(left,right):
            if left==right:
                return nums[left]

            mid=(left+right)//2

            left_sum=max_subarray_rec(left,mid)
            right_sum=max_subarray_rec(mid+1,right)
            cross_sum=max_crossing_sum(left,mid,right)
            return max(left_sum,right_sum,cross_sum)
        return max_subarray_rec(0,len(nums)-1)

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
solution=Solution()
result = solution.maxSubArray(nums)
print(result)