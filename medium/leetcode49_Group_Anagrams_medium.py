# #排序字符串作为键
# def groupAnagrams(strs):
#     anagram_map={}
#
#     for s in strs:
#         sorted_s=''.join(sorted(s))
#
#         if sorted_s not in anagram_map:
#             anagram_map[sorted_s]=[]
#
#         anagram_map[sorted_s].append(s)
#     return list(anagram_map.values())

#字符计数作为键
def groupAnagrams(strs):
    from collections import defaultdict

    anagram_map=defaultdict(list)

    for s in strs:
        count=[0]*26
        for char in s:
            count[ord(char)-ord('a')]+=1
        key=tuple(count)
        anagram_map[key].append(s)
    return list(anagram_map.values())

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
