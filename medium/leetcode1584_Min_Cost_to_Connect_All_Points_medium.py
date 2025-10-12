# import heapq
#
# class Solution:
#     def minCostConnectPoints(self,points):
#         """
#         Prim 算法 使用最小堆
#         """
#         n=len(points)
#         if n<=1:
#             return 0
#
#         #计算曼哈顿距离
#         def manhattan(i,j):
#             return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
#
#         #初始化
#         visited=[False]*n
#         min_heap=[] #distance,node
#         total_cost=0
#
#         #从节点0开始
#         visited[0]=True
#         current=0
#
#         #将节点0的所有边加入堆
#         for j in range(1,n):
#             distance=manhattan(0,j)
#             heapq.heappush(min_heap,(distance,j))
#
#         #构建MST
#         edges_used=0
#         while min_heap and edges_used<n-1:
#             distance,node=heapq.heappop(min_heap)
#
#             if visited[node]:
#                 continue
#             visited[node]=True
#             total_cost+=distance
#             edges_used+=1
#
#             #将新节点的所有边加入堆
#             for j in range(n):
#                 if not visited[j]:
#                     new_distance=manhattan(node,j)
#                     heapq.heappush(min_heap,(new_distance,j))
#         return total_cost

################################################################



import heapq


def minCostConnectPoints(points):
    """
    Prim算法的Python Tutor版本
    """
    n = len(points)
    if n <= 1:
        return 0

    print(f"点数量: {n}")
    print("点坐标:")
    for i, (x, y) in enumerate(points):
        print(f"  点{i}: ({x}, {y})")
    print()

    # 计算曼哈顿距离
    def manhattan(i, j):
        return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

    # 初始化变量
    visited = [False] * n  # 记录哪些点已加入MST
    min_heap = []  # 最小堆，存储(距离, 起点, 终点)
    total_cost = 0  # 总费用
    edges_used = 0  # 已使用的边数

    print("=== 初始化 ===")
    print(f"visited: {visited}")
    print(f"min_heap: {min_heap}")
    print(f"total_cost: {total_cost}")
    print(f"edges_used: {edges_used}")
    print()

    # 从点0开始
    print("=== 步骤1: 从点0开始 ===")
    visited[0] = True
    print(f"标记点0已访问")
    print(f"visited: {visited}")
    print()

    # 将点0的所有边加入堆
    print("=== 步骤2: 将点0的边加入堆 ===")
    for j in range(1, n):
        distance = manhattan(0, j)
        heapq.heappush(min_heap, (distance, 0, j))
        print(f"加入边: 0→{j}, 距离: {distance}")

    print(f"当前堆: {min_heap}")
    print()

    step = 0

    # Prim算法主循环
    while min_heap and edges_used < n - 1:
        step += 1
        print(f"=== 步骤{step + 2}: 选择第{edges_used + 1}条边 ===")

        # 弹出最小边
        distance, from_node, to_node = heapq.heappop(min_heap)
        print(f"弹出最小边: {from_node}→{to_node}, 距离: {distance}")
        print(f"当前堆: {min_heap}")

        if not visited[to_node]:
            # 接受这条边
            visited[to_node] = True
            total_cost += distance
            edges_used += 1

            print(f"✅ 接受边 {from_node}→{to_node}")
            print(f"标记点{to_node}已访问: {visited}")
            print(f"总费用更新: {total_cost}")
            print(f"已使用边数: {edges_used}")

            # 将新节点的边加入堆
            print(f"将点{to_node}的边加入堆:")
            for j in range(n):
                if not visited[j]:
                    new_distance = manhattan(to_node, j)
                    heapq.heappush(min_heap, (new_distance, to_node, j))
                    print(f"  加入边: {to_node}→{j}, 距离: {new_distance}")

            print(f"更新后堆: {min_heap}")
        else:
            print(f"❌ 跳过边 {from_node}→{to_node} (点{to_node}已访问)")

        print()

    print("=== 最终结果 ===")
    print(f"总费用: {total_cost}")
    print(f"已使用边数: {edges_used}")
    print(f"所有点是否访问: {all(visited)}")

    return total_cost


# 小型测试用例 - 适合Python Tutor
def test_small_case():
    """
    小型测试用例，适合在Python Tutor中运行
    """
    points = [
        [0, 0],  # 点0
        [2, 2],  # 点1
        [3, 10],  # 点2
        [5, 2],  # 点3
        [7, 0]  # 点4
    ]

    print("开始Prim算法演示")
    print("=" * 50)

    result = minCostConnectPoints(points)

    print("=" * 50)
    print(f"最终答案: {result}")

    return result


# 复制以下代码到 Python Tutor (https://pythontutor.com/)
test_small_case()