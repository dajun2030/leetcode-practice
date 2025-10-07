def characterReplacement(s, k):
    # 1. 初始化左边界 - 从字符串开头开始
    left = 0

    # 2. 初始化最大长度 - 记录全局最优解
    max_length = 0

    # 3. 初始化最大频率 - 跟踪窗口内最频繁字符的出现次数
    max_count = 0

    # 4. 初始化字符计数数组 - 高效统计字符频率
    char_count = [0] * 26

    # 5. 主循环：右指针遍历整个字符串
    for right in range(len(s)):
        # 6. 计算当前字符的索引（0-25）
        current_char = ord(s[right]) - ord('A')

        # 7. 更新当前字符的计数
        char_count[current_char] += 1

        # 8. 更新最大频率（可能比实际大，但算法正确）
        max_count = max(max_count, char_count[current_char])

        # 9. 检查窗口有效性：需要替换的字符数是否超过k
        #    窗口长度 - 最大频率 = 需要替换的字符数
        while (right - left + 1) - max_count > k:
            # 10. 收缩左边界：减少左端字符的计数
            left_char = ord(s[left]) - ord('A')
            char_count[left_char] -= 1

            # 11. 移动左指针
            left += 1

        # 12. 更新最大长度（此时窗口一定是有效的）
        max_length = max(max_length, right - left + 1)

    # 13. 返回全局最优解
    return max_length

# 单个测试用例
s = "AABABBA"
k = 1
result = characterReplacement(s, k)
print(f"输入: s='{s}', k={k}")
print(f"输出: {result}")
print(f"解释: 最长子串 'AABA' 可以通过替换1个字符变成 'AAAA'")