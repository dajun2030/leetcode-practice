# #方法1：使用字典/哈希表计数
# def findTheDifference(s, t):
#     char_count={}
#
#     for char in s:
#         char_count[char]=char_count.get(char,0)+1
#
#     for char in t:
#         # 检查条件：当前字符不在字典中 OR 当前字符的计数已经为0
#         # 这表示这个字符在t中出现的次数比在s中多
#         if char not in char_count or char_count[char]==0:
#             # 找到多出来的字符，立即返回
#             return char
#         # 如果字符在字典中且计数>0，说明这个字符在s中也存在
#         # 减少该字符的计数（表示匹配掉了一个）
#         char_count[char]-=1
#     return ''
#
# print(findTheDifference("abcd", "abcde"))
#
# #方法2：使用数组计数（更高效）
# def findTheDifference(s, t):
#     count=[0]*26
#
#     for char in s:
#         count[ord(char)-ord('a')]+=1
#
#     for char in t:
#         index=ord(char)-ord('a')
#         if count[index]==0:
#             return char
#         count[index]-=1
#     return ''
#
# print(findTheDifference("abcd", "abcde"))
#
# #使用异或运算找出不同的字符
# # def findTheDifference(s, t):
#     """
#     使用异或运算找出不同的字符
#
#     异或运算的特性：
#     1. a ^ a = 0      (相同数字异或为0)
#     2. a ^ 0 = a      (任何数字与0异或不变)
#     3. 异或满足交换律和结合律：a ^ b ^ c = a ^ c ^ b
#
#     思路：
#     将s和t中的所有字符进行异或运算，相同的字符会互相抵消变成0，
#     最后剩下的就是那个多出来的字符。
#     """
#
#     # 初始化异或结果为0
#     # 0与任何数异或都等于那个数本身
#     result = 0
#
#     # 第一步：遍历字符串s中的所有字符
#     # 将每个字符的ASCII码值与当前结果进行异或运算
#     for char in s:
#         # ord(char): 将字符转换为其对应的ASCII码值
#         # 例如：'a' -> 97, 'b' -> 98 等
#         # result ^= ord(char) 等价于 result = result ^ ord(char)
#         result ^= ord(char)
#         # 在这个过程中，s中所有字符的ASCII码值都在进行异或运算
#         # 由于异或的交换律，最终s中成对出现的字符会互相抵消
#
#     # 第二步：遍历字符串t中的所有字符
#     # 继续将每个字符的ASCII码值与上一步的结果进行异或运算
#     for char in t:
#         # 现在将t中所有字符的ASCII码值也加入异或运算
#         # 由于t比s多一个字符，且其他字符都与s相同（只是顺序不同）
#         # 所以相同的字符会两两抵消，最终剩下那个多出来的字符
#         result ^= ord(char)
#         # 数学原理：
#         # 假设 s = "abc", t = "abcd"
#         # 那么运算相当于：a^b^c ^ a^b^c^d = (a^a)^(b^b)^(c^c)^d = 0^0^0^d = d
#
#     # 第三步：将异或结果转换回字符
#     # chr(result): 将ASCII码值转换回对应的字符
#     # 例如：101 -> 'e', 121 -> 'y' 等
#     return chr(result)
# #
# # print(findTheDifference("abcd", "abcde"))

#方法4：使用集合和计数
def findTheDifference(s, t):
    from collections import Counter
    s_count=Counter(s)
    t_count=Counter(t)

    for char in t_count:
        if  char not in s_count or t_count[char]!=s_count[char]:
            return char
    return ''

print(findTheDifference("abcd", "abcde"))