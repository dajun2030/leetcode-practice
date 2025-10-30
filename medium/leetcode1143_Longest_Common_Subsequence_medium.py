# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         m, n = len(text1), len(text2)
#         # dp[i][j] 表示 text1[0:i] 和 text2[0:j] 的最长公共子序列长度
#         dp = [[0] * (n + 1) for _ in range(m + 1)]
#
#         for i in range(1, m + 1):
#             for j in range(1, n + 1):
#                 if text1[i - 1] == text2[j - 1]:
#                     dp[i][j] = dp[i - 1][j - 1] + 1
#                 else:
#                     dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
#
#         return dp[m][n]

def LCS_tutor():
    text1 = "abcde"
    text2 = "ace"

    print(f"问题: 最长公共子序列")
    print(f"字符串1: '{text1}'")
    print(f"字符串2: '{text2}'")
    print()

    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    print("初始化DP表 (处理空字符串情况):")
    print("    " + "  ".join([' '] + list(text2)))
    for i in range(m + 1):
        prefix = ' ' if i == 0 else text1[i - 1]
        print(f"{prefix} {dp[i]}")
    print()

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            char1, char2 = text1[i - 1], text2[j - 1]

            print(f"处理: text1[{i - 1}]='{char1}' vs text2[{j - 1}]='{char2}'")

            if char1 == char2:
                dp[i][j] = dp[i - 1][j - 1] + 1
                print(f"  ✅ 匹配! dp[{i}][{j}] = dp[{i - 1}][{j - 1}] + 1 = {dp[i - 1][j - 1]} + 1 = {dp[i][j]}")
            else:
                option1 = dp[i - 1][j]  # 忽略text1的当前字符
                option2 = dp[i][j - 1]  # 忽略text2的当前字符
                dp[i][j] = max(option1, option2)
                print(f"  ❌ 不匹配! 选择: max(忽略text1[{i - 1}]:{option1}, 忽略text2[{j - 1}]:{option2}) = {dp[i][j]}")

            print("  当前DP表:")
            print("    " + "  ".join([' '] + list(text2)))
            for idx in range(m + 1):
                prefix = ' ' if idx == 0 else text1[idx - 1]
                print(f"{prefix} {dp[idx]}")
            print()

    result = dp[m][n]
    print(f"🎯 最长公共子序列长度: {result}")

    # 找出具体的LCS（可选）
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            lcs.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    if lcs:
        lcs_str = ''.join(reversed(lcs))
        print(f"一个最长公共子序列: '{lcs_str}'")

    return result


# 运行
LCS_tutor()