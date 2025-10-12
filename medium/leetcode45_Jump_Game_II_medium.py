# class Solution(object):
#     def jump(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if nums is None or len(nums)==0:
#             return 0
#
#         step=0
#         left=0
#         right=0
#
#         for i in range(len(nums)-1):
#             right=max(right,i+nums[i])
#             if i==left:
#                 step+=1
#                 left=right
#         return step

#################################################
def jump_visualized(nums):
    print("🎯 Jump Game II 贪心算法可视化过程")
    print("=" * 60)
    print(f"数组: {nums}")
    print(f"长度: {len(nums)}")
    print("=" * 60)

    n = len(nums)
    if n <= 1:
        print("数组长度 <= 1，不需要跳跃")
        return 0

    jumps = 0
    current_end = 0
    farthest = 0

    print(f"初始状态: jumps={jumps}, current_end={current_end}, farthest={farthest}")
    print()

    for i in range(n - 1):
        print(f"位置 {i}: 可以跳到位置 {i}~{i + nums[i]}")

        # 更新最远位置
        old_farthest = farthest
        farthest = max(farthest, i + nums[i])

        if farthest > old_farthest:
            print(f"  更新 farthest: {old_farthest} → {farthest}")
        else:
            print(f"  farthest 保持不变: {farthest}")

        # 检查是否需要跳跃
        if i == current_end:
            jumps += 1
            old_end = current_end
            current_end = farthest

            print(f"  🎯 到达跳跃边界 i={i} == current_end={old_end}")
            print(f"  跳跃次数: {jumps}")
            print(f"  新的跳跃边界: current_end={current_end}")

            # 检查是否到达终点
            if current_end >= n - 1:
                print(f"  ✅ 可以到达终点 (current_end={current_end} >= n-1={n - 1})")
                break
        else:
            print(f"  继续前进 (i={i} < current_end={current_end})")

        print()

    print(f"\n🎊 最终结果: 最少需要 {jumps} 次跳跃")
    return jumps


# 运行可视化
print("可视化演示:")
jump_visualized([2, 3, 1, 1, 4])