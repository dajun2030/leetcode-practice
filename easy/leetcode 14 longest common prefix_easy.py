# 垂直扫描法
# def longestCommonPrefix(strs):
#     # 边界情况处理：如果字符串数组为空，直接返回空字符串
#     if not strs:
#         return ""
#
#     # 以第一个字符串作为初始的公共前缀基准
#     prefix = strs[0]
#
#     # 遍历第一个字符串的每一个字符位置
#     for i in range(len(prefix)):
#         # 获取当前位置要比较的字符
#         current_char = prefix[i]
#
#         # 遍历数组中除第一个字符串外的所有其他字符串
#         for s in strs[1:]:
#             # 情况1：当前字符串s的长度已经不够了（小于等于当前位置i）
#             # 情况2：当前字符串s在位置i的字符与基准字符不匹配
#             if i >= len(s) or s[i] != current_char:
#                 # 返回从开头到当前位置的前一个位置的前缀
#                 # 因为当前位置的字符已经不匹配了
#                 return prefix[:i]
#
#     # 如果整个循环完成，说明第一个字符串就是最长公共前缀
#     return prefix
#
#
#
#
# def longestCommonPrefix(strs):
#     if not strs:
#         return ""
#
#     # 垂直扫描：逐个字符位置比较所有字符串
#     for i in range(len(strs[0])):
#         char = strs[0][i]  # 基准字符
#
#         # 检查所有其他字符串在相同位置的字符
#         for j in range(1, len(strs)):
#             # 如果长度不够或字符不匹配
#             if i >= len(strs[j]) or strs[j][i] != char:
#                 return strs[0][:i]  # 返回当前已验证的前缀
#
#     return strs[0]  # 第一个字符串就是完整前缀
# print(longestCommonPrefix(["flower", "flow", "flight"]))

#集合
# def longestCommonPrefix(strs):
#     """
#     :type strs: List[str]
#     :rtype: str
#     """
#     # 初始化结果字符串为空，用于存储公共前缀
#     result = ""
#
#     # 初始化字符位置指针，从每个字符串的第0个字符开始比较
#     i = 0
#
#     # 无限循环，直到满足退出条件
#     while True:
#         try:
#             # 关键行：创建所有字符串在第i个位置的字符集合
#             # 使用生成器表达式遍历strs中每个字符串的第i个字符
#             # 例如：strs = ["flower","flow","flight"], i=0 时
#             # sets = {'f', 'f', 'f'} → 实际存储为 {'f'}（集合自动去重）
#             sets = set(string[i] for string in strs)
#
#             # 判断集合的大小：
#             # 如果len(sets)==1，说明所有字符串在第i位置都有相同的字符
#             # 如果len(sets)>1，说明至少有两个字符串在第i位置的字符不同
#             if len(sets) == 1:
#                 # 从集合中取出唯一的字符添加到结果中
#                 # sets.pop() 移除并返回集合中的任意元素，这里只有一个元素
#                 result += sets.pop()
#
#                 # 指针移动到下一个字符位置
#                 i += 1
#             else:
#                 # 发现字符不匹配，立即退出循环
#                 break
#
#         except Exception as e:
#             # 异常处理：当任何字符串的长度不足时（即i >= len(string)）
#             # 会抛出IndexError，这里捕获所有异常并退出循环
#             # 例如：当i=4时，"flow"只有4个字符，访问string[4]会越界
#             break
#
#     # 返回找到的最长公共前缀
#     return result
#
# print(longestCommonPrefix(["flower", "flow", "flight"]))
###################################################################
#水平扫描
def longestCommonPrefix(strs):
    # 第1行：边界情况检查 - 如果输入列表为空，直接返回空字符串
    if not strs:
        return ""

    # 第2行：初始化前缀 - 将第一个字符串作为初始的公共前缀候选
    prefix = strs[0]

    # 第3行：开始水平扫描 - 从第二个字符串开始遍历（索引1到末尾）
    for i in range(1, len(strs)):
        # 第4行：获取当前要比较的字符串
        current_str = strs[i]

        # 第5-9行：调整前缀直到匹配当前字符串
        # 第5行：循环条件 - 当前字符串不以当前前缀开头时继续调整
        while not current_str.startswith(prefix):
            # 第6行：缩短前缀 - 去掉最后一个字符
            prefix = prefix[:-1]

            # 第7-8行：边界检查 - 如果前缀被缩短为空字符串，立即返回
            if not prefix:
                return ""
        # 第9行：while循环结束 - 此时prefix已是当前字符串的前缀

    # 第10行：返回最终找到的最长公共前缀
    return prefix

print(longestCommonPrefix(["flower", "flow", "flight"]))
