# import re
# def isPalindrome(s: str):
#     new_s=re.sub(r'[^A-Za-z]','',s).lower()
#     n=len(new_s)
#     left,right=0,n-1
#
#     while left<=right:
#         if new_s[left] != new_s[right]:
#             return False
#         right-=1
#         left+=1
#
#     return True

def isPalindrome(s: str):
    n=len(s)
    left,right=0,n-1

    while left<right:
        while left<right and not s[left].isalnum():
            left+=1

        while left<right and not s[right].isalnum():
            right-=1

        if s[left].lower()!=s[right].lower():
            return False
        left+=1
        right-=1
    return True

print(isPalindrome("0P"))