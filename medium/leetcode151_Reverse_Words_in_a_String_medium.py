# def reverseWords(s):
#     li=s.strip().split()
#     result=[]
#     for i in range(len(li)-1,-1,-1):
#         result.append(li[i])
#
#     return ' '.join(result)


#
# def reverseWords(s):
#     return ' '.join(s.split()[::-1])

#左右指针法
def reverseWords(s):
    s=s.strip()
    words=[]
    left,right=len(s)-1,len(s)-1

    while left>=0:
        while left>=0 and s[left]==' ':
            left-=1
            right-=1

        while left>=0 and s[left]!=' ':
            left-=1

        word=s[left+1:right+1]
        words.append(word)

        right=left

    return ' '.join(words)
print(reverseWords('how are you'))