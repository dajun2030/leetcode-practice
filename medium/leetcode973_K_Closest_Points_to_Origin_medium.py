# import heapq
# import math
#
# class Solution:
#     def kClosest(self, points, k):
#         max_heap=[]
#
#         for point in points:
#             distance=point[0]**2+point[1]**2
#             if len(max_heap)<k:
#                 heapq.heappush(max_heap,(-distance,point))
#             else:
#                 if distance<-max_heap[0][0]:
#                     heapq.heappushpop(max_heap,(-distance,point))
#         return [point for neg_dist,point in max_heap]


import heapq


class Solution:
    def kClosest(self, points, k):
        max_heap = []

        for point in points:
            dist_sq = point[0] ** 2 + point[1] ** 2

            if len(max_heap) < k:
                heapq.heappush(max_heap, (-dist_sq, point))
            else:
                if dist_sq < -max_heap[0][0]:
                    heapq.heappushpop(max_heap, (-dist_sq, point))

        return [point for _, point in max_heap]


def test_kClosest():
    solution = Solution()

    test_cases = [
        ([[1, 3], [-2, 2]], 1, [[-2, 2]]),
        ([[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]]),
        ([[0, 1], [1, 0]], 2, [[0, 1], [1, 0]]),
        ([[1, 1], [2, 2], [3, 3], [4, 4]], 2, [[1, 1], [2, 2]]),
        ([[2, 2], [2, 2], [3, 3], [2, -2], [1, 1]], 4, [[2, 2], [2, 2], [2, -2], [1, 1]])
    ]

    print("🧪 K Closest Points 测试")
    print("=" * 50)

    all_passed = True
    for i, (points, k, expected) in enumerate(test_cases, 1):
        result = solution.kClosest(points, k)
        # 排序结果以便比较（顺序不重要）
        result_sorted = sorted(result)
        expected_sorted = sorted(expected)
        status = "✅" if result_sorted == expected_sorted else "❌"
        print(f"测试 {i}: points={points}, k={k}")
        print(f"  结果: {result} {status}")
        print(f"  期望: {expected}")

        if result_sorted != expected_sorted:
            all_passed = False

    print(f"\n总体结果: {'✅ 所有测试通过!' if all_passed else '❌ 有测试失败!'}")


# 运行测试
test_kClosest()