import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        count=Counter(nums)

        min_heap=[]
        for num,freq in count.items():
            if len(min_heap)<k:
                heapq.heappush(min_heap,(freq,num))
            else:
                if freq>min_heap[0][0]:
                    heapq.heappushpop(min_heap,(freq,num))

        return[num for freq,num in min_heap]


def test_topKFrequent():
    solution = Solution()

    test_cases = [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        ([1, 1, 1, 2, 2, 3, 3, 3, 3], 2, [3, 1]),
        ([4, 1, -1, 2, -1, 2, 3], 2, [-1, 2])
    ]

    for nums, k, expected in test_cases:
        result = solution.topKFrequent(nums, k)
        # 排序结果以便比较（顺序不重要）
        result_sorted = sorted(result)
        expected_sorted = sorted(expected)
        status = "✅" if result_sorted == expected_sorted else "❌"
        print(f"nums={nums}, k={k} -> {result} {status} (expected: {expected})")


# 运行测试
test_topKFrequent()