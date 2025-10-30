def strStr(haystack, needle):
    if not needle:
        return 0

    n,m=len(haystack),len(needle)
    for i in range(n-m+1):
        if haystack[i:i+m]==needle:
            return i

    return -1

print(strStr('hello', 'll'))
print(strStr('abbacde', 'bba'))
print(strStr('abbacde', ''))