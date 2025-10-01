# def reverseString(s):
#     n=len(s)
#
#     for i in range(n//2):
#         s[i],s[n-i-1]=s[n-i-1],s[i]
#
#

def reverseString(s):
    n=len(s)
    left,right=0,n-1

    while left<=right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1

test_cases = [
        ["h", "e", "l", "l", "o"],
        ["H", "a", "n", "n", "a", "h"],
        ["a", "b"]]

for i,s in enumerate(test_cases):
    original=s.copy()
    reverseString(s)
    print(f"测试用例:{i+1}")
    print(f"原始：{original}")
    print(f"反转：{s}")
    print()



