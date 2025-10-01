# from collections import defaultdict
# def canConstruct(ransomNote: str, magazine: str):
#     if len(ransomNote)>len(magazine):
#         return False
#     strnums=defaultdict(int)
#
#     for char in magazine:
#         strnums[char]+=1
#
#     for char in ransomNote:
#         strnums[char]-=1
#         if  strnums[char]<0:
#             return False
#     return True


def canConstruct(ransomNote: str, magazine: str):
    from collections import Counter
    ransomcount=Counter(ransomNote)
    magazinecount=Counter(magazine)

    for char in ransomcount:
        if magazinecount[char]<ransomcount[char]:
            return False
    return True

print(canConstruct("abb","cdabcdbabb"))
print(canConstruct("abcd","cdabdcbaabedcd"))
