def checkInclusion(s1, s2):
    if len(s1)>len(s2):
        return False

    s1_count=[0]*26
    s2_count=[0]*26

    for i in range(len(s1)):
        s1_count[ord(s1[i])-ord('a')]+=1
        s2_count[ord(s2[i])-ord('a')]+=1

    if s1_count==s2_count:
        return True

    for i in range(len(s1),len(s2)):
        left_char=ord(s2[i-len(s1)])-ord('a')
        s2_count[left_char]-=1

        right_char=ord(s2[i])-ord('a')
        s2_count[right_char]+=1

        if s1_count==s2_count:
            return True
    return False

test_cases = [
    ("ab", "eidbaooo", True),     # "ba" 是 "ab" 的排列
    ("ab", "eidboaoo", False),    # 没有包含 "ab" 排列的子串
    ("abc", "bbbca", True),       # "bca" 是 "abc" 的排列
    ("a", "a", True),             # 单个字符相同
    ("a", "b", False),            # 单个字符不同
    ("adc", "dcda", True),        # "dcd" 不是，"cda" 是排列
]

for s1, s2, expected in test_cases:
    result = checkInclusion(s1, s2)
    print(f"s1='{s1}', s2='{s2}' -> {result} (期望: {expected})")
