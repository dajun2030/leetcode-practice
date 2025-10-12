# def combinations(digits):
#     if not digits:
#         return []
#
#     phone_map = {
#         '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
#         '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
#     }
#
#     result=[]
#     def backtrack(index,path):
#         if index==len(digits):
#             result.append(''.join(path))
#             return
#
#         current_letter=phone_map[digits[index]]
#
#         for letter in current_letter:
#             path.append(letter)
#             backtrack(index+1,path)
#             path.pop()
#     backtrack(0,[])
#     return result

#########################################################
def letterCombinations_visualized(digits):
    print("🎯 Letter Combinations 回溯法可视化过程")
    print("=" * 60)
    print(f"输入数字: '{digits}'")

    # 数字到字母的映射
    phone_map = {
        '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
        '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
    }
    print(f"字母映射: {phone_map}")
    print("=" * 60)

    result = []

    def backtrack(index, path, depth):
        indent = "  " * depth

        print(f"{indent}↳ backtrack(index={index}, path={path})")

        # 如果处理完所有数字
        if index == len(digits):
            combination = "".join(path)
            result.append(combination)
            print(f"{indent}  ✅ 找到组合: '{combination}'")
            return

        # 当前数字和对应的字母
        current_digit = digits[index]
        letters = phone_map[current_digit]

        print(f"{indent}  数字 '{current_digit}' 对应字母: '{letters}'")

        # 遍历所有可能的字母
        for letter in letters:
            print(f"{indent}    🔄 考虑字母: '{letter}'")

            # 选择当前字母
            path.append(letter)
            print(f"{indent}      ➕ 选择 '{letter}' → path={path}")

            # 递归处理下一个数字
            backtrack(index + 1, path, depth + 1)

            # 回溯
            removed = path.pop()
            print(f"{indent}      ➖ 回溯 '{removed}' → path={path}")

    if digits:
        backtrack(0, [], 0)
    else:
        print("输入为空，返回空列表")

    print(f"\n🎊 最终结果 ({len(result)} 个组合):")
    for i, comb in enumerate(result):
        print(f"  {i + 1:2d}. '{comb}'")

    return result


# 运行可视化
print("可视化演示:")
letterCombinations_visualized("23")