# def reverseString(s):
#     n=len(s)
#
#     for i in range(n//2):
#         s[i],s[n-i-1]=s[n-i-1],s[i]
#
#

# def reverseString(s):
#     n=len(s)
#     left,right=0,n-1
#
#     while left<=right:
#         s[left],s[right]=s[right],s[left]
#         left+=1
#         right-=1
#
# test_cases = [
#         ["h", "e", "l", "l", "o"],
#         ["H", "a", "n", "n", "a", "h"],
#         ["a", "b"]]
#
# for i,s in enumerate(test_cases):
#     original=s.copy()
#     reverseString(s)
#     print(f"测试用例:{i+1}")
#     print(f"原始：{original}")
#     print(f"反转：{s}")
#     print()
#################################################################

def reverseString(s_new):
    """
    递归方法反转字符串
    """
    s=list(s_new)
    def helper(left, right):
        # 基准情况：指针相遇或交叉
        if left >= right:
            return
        # 交换当前层的字符
        s[left], s[right] = s[right], s[left]
        # 递归处理内层
        helper(left + 1, right - 1)

    helper(0, len(s) - 1)
    return ''.join(s)

print(reverseString('hello world'))