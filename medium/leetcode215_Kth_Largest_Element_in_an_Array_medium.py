import heapq

class Solution:
    def findKthLargest(self, nums, k) :
        min_heap=[]

        for num in nums:
            if len(min_heap)<k:
                heapq.heappush(min_heap,num)
            else:
                if num>min_heap[0]:
                    heapq.heappushpop(min_heap,num)
        return min_heap[0]


def test_findKthLargest():
    solution = Solution()

    test_cases = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([1], 1, 1),
        ([2, 1], 2, 1),
        ([7, 6, 5, 4, 3, 2, 1], 5, 3)
    ]

    for nums, k, expected in test_cases:
        result = solution.findKthLargest(nums, k)
        status = "✅" if result == expected else "❌"
        print(f"nums={nums}, k={k} -> {result} {status} (expected: {expected})")


# 运行测试
test_findKthLargest()