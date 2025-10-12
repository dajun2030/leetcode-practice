# import heapq
#
# def lastStoneWeight(stones):
#     max_heap=[-stone for stone in stones]
#     heapq.heapify(max_heap)
#
#     while len(max_heap)>1:
#         heavist=-heapq.heappop(max_heap)
#         second_heavist=-heapq.heappop(max_heap)
#
#         if heavist!=second_heavist:
#             heapq.heappush(max_heap,-(heavist-second_heavist))
#     return -max_heap[0] if max_heap else 0

import heapq


def lastStoneWeight_with_trace(stones):
    max_heap = [-stone for stone in stones]
    heapq.heapify(max_heap)
    print(f"初始堆: {max_heap}")

    step = 1
    while len(max_heap) > 1:
        # 取出最重的两块石头
        stone1 = -heapq.heappop(max_heap)
        stone2 = -heapq.heappop(max_heap)
        print(f"\n第{step}轮: 取出 {stone1} 和 {stone2}")

        if stone1 != stone2:
            new_stone = stone1 - stone2
            print(f"  产生新石头: {new_stone}")

            # 关键操作：插入新石头
            print(f"  插入前堆: {max_heap}")
            heapq.heappush(max_heap, -new_stone)
            print(f"  插入后堆: {max_heap} (最重石头: {-max_heap[0]})")
        else:
            print(f"  完全粉碎，无剩余")

        step += 1

    return -max_heap[0] if max_heap else 0


# 测试
stones = [2, 7, 4, 1, 8, 1]
result = lastStoneWeight_with_trace(stones)
print(f"\n最终结果: {result}")
