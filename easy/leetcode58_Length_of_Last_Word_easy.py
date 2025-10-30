# def lengthOfLastWord(s):
#     words=s.split()
#     length=len(words[-1])
#     return length
#
# print(lengthOfLastWord('hello who are you. i know everything '))

#方法一：从后往前遍历
# def lengthOfLastWord(s) :
#     length=0
#     i=len(s)-1
#
#     while i>=0 and s[i]==' ':
#         i-=1
#
#     while i>=0 and s[i]!=' ':
#         length+=1
#         i-=1
#     return length
#
# print(lengthOfLastWord('hello who are you. i know everything '))

#一行代码
# def lengthOfLastWord(s) :
#     return len(s.strip().split(" ")[-1])
#
# print(lengthOfLastWord('hello who are you. i know everything '))

def lengthOfLastWord(s):
    count = 0
    local_count = 0

    for i in range(len(s)):
        if s[i] == ' ':
            local_count = 0
        else:
            local_count += 1
            count = local_count
    return count

print(lengthOfLastWord('hello world'))