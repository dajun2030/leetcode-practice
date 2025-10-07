# def lengthOfLongestSubstring(s):
#     if not s:
#         return 0
#
#     left=0
#     max_length=0
#     char_index= {}
#
#     for right in range(len(s)):
#         current_char=s[right]
#
#         if current_char in char_index and char_index[current_char]>=left:
#             left=char_index[current_char]+1
#         char_index[current_char]=right
#
#         max_length=max(max_length,right-left+1)
#     return max_length

def lengthOfLongestSubstring(s):
    res=0
    arr=[]

    for i in s:
        while i in arr:
            arr.pop(0)
        arr.append(i)
        res=max(res,len(arr))
    return res

print(lengthOfLongestSubstring("abcabcbb"))