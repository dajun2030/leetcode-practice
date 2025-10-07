def minEatingSpeed(piles, h):
    # 第1行：计算所有香蕉的总数
    total = sum(piles)

    # 第2行：计算理论最小速度
    # (total + h - 1) // h 是向上取整的除法，表示如果均匀分配，每小时至少需要吃多少根
    # max(1, ...) 确保最小速度至少为1
    left = max(1, (total + h - 1) // h)  # 理论最小速度

    # 第3行：最大速度就是最大堆的香蕉数
    # 因为如果一堆有max(piles)根，最坏情况需要1小时吃完这一堆
    right = max(piles)  # 最大速度

    # 第5-6行：特殊情况处理
    # 如果时间h刚好等于香蕉堆数，意味着每堆必须正好在1小时内吃完
    # 因此速度必须至少等于最大堆的香蕉数
    if h == len(piles):
        return right

    # 第8行：开始二分查找
    # 条件 left < right 表示当左右指针相遇时停止
    while left < right:
        # 第9行：计算中间速度，防止整数溢出
        mid = left + (right - left) // 2

        # 第10行：初始化需要的小时数
        hours_needed = 0

        # 第13-16行：计算以速度mid吃完所有香蕉需要的时间
        for pile in piles:
            # (pile + mid - 1) // mid 是向上取整的整数除法
            # 等价于 math.ceil(pile / mid)，但更快
            hours_needed += (pile + mid - 1) // mid

            # 如果已经超过规定时间h，提前终止循环
            # 这是一个重要的优化，避免不必要的计算
            if hours_needed > h:
                break

        # 第18-21行：根据计算结果调整搜索范围
        if hours_needed <= h:
            # 当前速度足够快，尝试更小的速度
            # 注意：right = mid 而不是 mid - 1，因为mid可能是答案
            right = mid
        else:
            # 当前速度太慢，需要更大的速度
            # left = mid + 1 因为mid肯定不是答案
            left = mid + 1

    # 第23行：返回最小可行速度
    # 此时 left == right，就是我们要找的最小速度
    return left


# 测试用例
test_cases = [
    ([3, 6, 7, 11], 8),  # 输出: 4
    ([30, 11, 23, 4, 20], 5),  # 输出: 30
    ([30, 11, 23, 4, 20], 6),  # 输出: 23
    ([312884470], 312884469),  # 输出: 2
    ([1, 1, 1, 1], 4),  # 输出: 1
    ([1000000000], 2),  # 输出: 500000000
    ([1000000000, 1000000000, 1000000000], 3),  # 输出: 1000000000
]

for piles, h in test_cases:
    result = minEatingSpeed(piles, h)
    print(f"piles = {piles}, h = {h}, k = {result}")