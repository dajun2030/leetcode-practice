from collections import deque
import time


class Solution:
    def pacificAtlantic(self, heights):
        """
        带可视化的太平洋大西洋水流问题解法
        """
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])

        print("初始网格:")
        self.print_grid(heights, "高度网格")
        print()

        # 初始化访问矩阵
        pacific_visited = [[False] * n for _ in range(m)]
        atlantic_visited = [[False] * n for _ in range(m)]

        # 初始化队列
        pacific_queue = deque()
        atlantic_queue = deque()

        # 标记太平洋边界
        print("标记太平洋边界（左边界和上边界）:")
        for i in range(m):
            pacific_queue.append((i, 0))
            pacific_visited[i][0] = True
            print(f"  太平洋边界加入: ({i}, 0)")
        for j in range(n):
            pacific_queue.append((0, j))
            pacific_visited[0][j] = True
            print(f"  太平洋边界加入: (0, {j})")

        print("\n标记大西洋边界（右边界和下边界）:")
        for i in range(m):
            atlantic_queue.append((i, n - 1))
            atlantic_visited[i][n - 1] = True
            print(f"  大西洋边界加入: ({i}, {n - 1})")
        for j in range(n):
            atlantic_queue.append((m - 1, j))
            atlantic_visited[m - 1][j] = True
            print(f"  大西洋边界加入: ({m - 1}, {j})")

        print("\n初始太平洋访问状态:")
        self.print_visited(pacific_visited, "太平洋")

        print("\n初始大西洋访问状态:")
        self.print_visited(atlantic_visited, "大西洋")

        # BFS 函数
        def bfs(queue, visited, ocean_name):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            step = 0

            while queue:
                step += 1
                print(f"\n{ocean_name} BFS 第 {step} 步:")
                print(f"  当前队列: {list(queue)}")

                x, y = queue.popleft()
                print(f"  处理位置: ({x}, {y}), 高度: {heights[x][y]}")

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                        if heights[nx][ny] >= heights[x][y]:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                            print(f"    标记 ({nx}, {ny}), 高度: {heights[nx][ny]} ≥ {heights[x][y]}")
                        else:
                            print(f"    跳过 ({nx}, {ny}), 高度: {heights[nx][ny]} < {heights[x][y]}")

                # 显示当前访问状态
                self.print_visited(visited, f"{ocean_name} 当前状态")
                time.sleep(0.5)  # 暂停以便观察

        print("\n" + "=" * 50)
        print("开始太平洋 BFS 搜索...")
        print("=" * 50)
        bfs(pacific_queue, pacific_visited, "太平洋")

        print("\n" + "=" * 50)
        print("开始大西洋 BFS 搜索...")
        print("=" * 50)
        bfs(atlantic_queue, atlantic_visited, "大西洋")

        # 收集结果
        result = []
        print("\n" + "=" * 50)
        print("收集最终结果...")
        print("=" * 50)

        for i in range(m):
            for j in range(n):
                if pacific_visited[i][j] and atlantic_visited[i][j]:
                    result.append([i, j])
                    print(f"找到结果位置: ({i}, {j})")

        print(f"\n最终结果数量: {len(result)}")
        print(f"结果坐标: {result}")

        return result

    def print_grid(self, grid, title):
        """打印网格"""
        print(f"{title}:")
        for row in grid:
            print("  " + " ".join(f"{num:2d}" for num in row))

    def print_visited(self, visited, title):
        """打印访问状态"""
        print(f"{title}:")
        for row in visited:
            print("  " + " ".join(" T" if cell else " F" for cell in row))


# 测试用例
def test_small_case():
    """小型测试用例，便于观察"""
    print("小型测试用例")
    print("=" * 60)

    heights = [
        [1, 2, 3],
        [4, 5, 4],
        [3, 2, 1]
    ]

    solution = Solution()
    result = solution.pacificAtlantic(heights)
    return result


def test_original_case():
    """原始测试用例"""
    print("\n" + "=" * 60)
    print("原始测试用例")
    print("=" * 60)

    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4]
    ]

    solution = Solution()
    result = solution.pacificAtlantic(heights)
    return result


# 运行测试
if __name__ == "__main__":
    # 运行小型测试用例（推荐用于观察）
    test_small_case()

    # 如果想要运行原始测试用例，取消下面的注释
    # test_original_case()