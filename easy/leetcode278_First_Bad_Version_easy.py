# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    # 这是模拟的API，实际使用时会有真正的实现
    # 这里我们假设第一个坏版本是4
    FIRST_BAD = 4
    return version >= FIRST_BAD


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


# 测试代码
if __name__ == "__main__":
    solution = Solution()

    # 测试用例1: n=5, 第一个坏版本应该是4
    result1 = solution.firstBadVersion(5)
    print(f"n=5时第一个坏版本: {result1}")  # 应该输出4

    # 测试用例2: n=1, 只有1个版本且是坏的
    result2 = solution.firstBadVersion(1)
    print(f"n=1时第一个坏版本: {result2}")  # 应该输出1

    # 测试用例3: n=10, 第一个坏版本是4
    result3 = solution.firstBadVersion(10)
    print(f"n=10时第一个坏版本: {result3}")  # 应该输出4