import heapq


def networkDelayTime(times, n, k):
    """
    Python Tutor专用简化版本
    """
    # 构建邻接表
    graph = [[] for _ in range(n + 1)]
    for u, v, w in times:
        graph[u].append((v, w))

    # 初始化距离数组
    dist = [float('inf')] * (n + 1)
    dist[k] = 0

    # 最小堆
    heap = [(0, k)]

    while heap:
        current_dist, node = heapq.heappop(heap)

        # 如果当前距离不是最短距离，跳过
        if current_dist > dist[node]:
            continue

        # 更新邻居节点的距离
        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    # 找出最大距离
    max_time = max(dist[1:])
    return max_time if max_time < float('inf') else -1


# Python Tutor测试代码
def test_python_tutor():
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2

    result = networkDelayTime(times, n, k)
    print("结果:", result)
    return result


# 复制以下代码到Python Tutor
test_python_tutor()