class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(start, path):
            # 将当前路径加入结果
            result.append(path[:])

            # 从start开始遍历，避免重复
            for i in range(start, len(nums)):
                # 选择当前元素
                path.append(nums[i])
                # 递归探索后续元素
                backtrack(i + 1, path)
                # 回溯，撤销选择
                path.pop()

        result = []
        backtrack(0, [])
        return result


def test_subsets():
    solution = Solution()

    test_cases = [
        ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
        ([0], [[], [0]]),
        ([1, 2], [[], [1], [2], [1, 2]]),
        ([1, 2, 3, 4], [])  # 不检查具体内容，只检查长度
    ]

    print("🧪 Subsets 测试")
    print("=" * 50)

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.subsets(nums)

        # 排序结果以便比较（顺序不重要）
        result_sorted = sorted([sorted(subset) for subset in result])
        expected_sorted = sorted([sorted(subset) for subset in expected])

        if nums == [1, 2, 3, 4]:
            # 对于大测试用例，只检查长度
            status = "✅" if len(result) == 16 else "❌"
            print(f"测试 {i}: nums={nums}")
            print(f"  结果长度: {len(result)} {status}")
            print(f"  期望长度: 16")
        else:
            status = "✅" if result_sorted == expected_sorted else "❌"
            print(f"测试 {i}: nums={nums}")
            print(f"  结果: {result} {status}")
            print(f"  期望: {expected}")
        print()


# 运行测试
test_subsets()


def subsets_visualized(nums):
    print("🎯 Subsets 回溯法可视化过程")
    print("=" * 60)
    print(f"输入数组: {nums}")
    print("=" * 60)

    result = []

    def backtrack(start, path, depth):
        # 缩进显示递归深度
        indent = "  " * depth

        # 记录当前状态
        print(f"{indent}↳ backtrack(start={start}, path={path})")

        # 将当前路径加入结果
        result.append(path[:])
        print(f"{indent}  添加到结果: {path}")

        # 从start开始遍历
        for i in range(start, len(nums)):
            print(f"{indent}  循环 i={i}, 选择 nums[{i}] = {nums[i]}")

            # 选择当前元素
            path.append(nums[i])
            print(f"{indent}     path添加: {path}")

            # 递归探索后续元素
            backtrack(i + 1, path, depth + 1)

            # 回溯，撤销选择
            removed = path.pop()
            print(f"{indent}     path回溯: 移除 {removed} → {path}")

    backtrack(0, [], 0)

    print(f"\n🎊 最终结果 ({len(result)} 个子集):")
    for i, subset in enumerate(result):
        print(f"  {i + 1:2d}. {subset}")

    return result


# 运行可视化
print("可视化演示:")
subsets_visualized([1, 2, 3])