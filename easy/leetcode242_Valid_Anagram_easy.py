#哈希计数法
# def isAnagram(s: str, t: str):
#     if len(s) != len(t):
#         return False
#
#     char_count={}
#     for char in s:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
#
#     for char in t:
#         if char not in char_count or char_count[char] == 0:
#             return False
#         char_count[char]-=1
#     return True

#思路2：数组计数法
# def isAnagram(s: str, t: str):
#     if len(s)!=len(t):
#         return False
#
#     count=[0]*26
#     for char in s :
#         count[ord(char)-ord('a')]+=1
#
#     for char in t:
#         index=ord(char)-ord('a')
#         count[index]-=1
#         if count[index]<0:
#             return False
#     return True

#思路3：排序比较法
# def isAnagram(s: str, t: str):
#     if len(s)!=len(t):
#         return False
#
#     s_sorted=sorted(s)
#     t_sorted=sorted(t)
#
#     return s_sorted==t_sorted

#思路4 Counter
def isAnagram(s: str, t: str):
    from collections import Counter

    if len(s) != len(t):
        return False

    s_count = Counter(s)
    t_count = Counter(t)

    return s_count == t_count

print(isAnagram("",""))
print(isAnagram("","c"))
print(isAnagram("ba","ab"))
print(isAnagram("ed","cd"))
print(isAnagram("abdc","abcd"))
print(isAnagram("aacc","ccac"))

