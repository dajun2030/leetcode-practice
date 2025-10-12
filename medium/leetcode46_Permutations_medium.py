# def permute(nums):
#     result = []
#
#     def backtrack(path, used):
#         # 如果路径长度等于数组长度，说明找到一个排列
#         if len(path) == len(nums):
#             result.append(path[:])
#             return
#
#         # 遍历所有数字
#         for i in range(len(nums)):
#             # 如果数字没有被使用过
#             if not used[i]:
#                 # 选择当前数字
#                 used[i] = True
#                 path.append(nums[i])
#
#                 # 递归探索
#                 backtrack(path, used)
#
#                 # 回溯，撤销选择
#                 path.pop()
#                 used[i] = False
#
#     used = [False] * len(nums)
#     backtrack([], used)
#     return result
#
#
# # 测试
# print("排列结果:", permute([1, 2, 3]))

def permute_debug(nums):
    result = []
    call_count = [0]  # 用于计数递归调用

    def backtrack(path, used, depth):
        call_count[0] += 1
        call_id = call_count[0]
        indent = "  " * depth

        print(indent + "调用#" + str(call_id) + ": backtrack(path=" + str(path) + ", used=" + str(used) + ")")

        # 终止条件
        if len(path) == len(nums):
            result.append(path[:])
            print(indent + "  ✅ 找到完整排列: " + str(path))
            return

        # 遍历所有数字
        for i in range(len(nums)):
            if not used[i]:
                print(indent + "  🔄 考虑数字: nums[" + str(i) + "] = " + str(nums[i]))

                # 选择
                used[i] = True
                path.append(nums[i])
                print(indent + "    ➕ 选择 " + str(nums[i]) + " → path=" + str(path) + ", used=" + str(used))

                # 递归
                backtrack(path, used, depth + 1)

                # 回溯
                path.pop()
                used[i] = False
                print(indent + "    ➖ 回溯 " + str(nums[i]) + " → path=" + str(path) + ", used=" + str(used))

    used = [False] * len(nums)
    print("开始生成排列...")
    backtrack([], used, 0)

    print("\n🎊 最终结果 (" + str(len(result)) + " 个排列):")
    for i, perm in enumerate(result):
        print("  " + str(i + 1) + ". " + str(perm))

    return result


# 运行调试版本（使用小数组便于理解）
print("调试演示 [1, 2,3]:")
permute_debug([1, 2,3])