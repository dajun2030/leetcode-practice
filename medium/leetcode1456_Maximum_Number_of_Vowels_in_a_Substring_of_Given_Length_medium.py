def maxVowels(s, k):
    if not s or len(s)==0 or len(s)<k:
        return 0

    max_count=0
    vowels={'a','e','i','o','u'}
    current_count=0
    #初始化窗口
    for i in range(k):
        if s[i] in vowels:
            current_count+=1
    max_count=current_count

    #遍历后续字符
    for j in range(k,len(s)):
        left_char=s[j-k]
        if left_char in vowels:
            current_count-=1

        right_char=s[j]
        if right_char in vowels:
            current_count+=1

        max_count=max(current_count,max_count)

    return max_count

print(maxVowels('abcde', 3))
print(maxVowels('abciiidef', 3))