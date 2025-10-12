#Python Tutor 兼容版本 (BFS)
from collections import deque
def numIslands_simple(grid):
    if not grid :
        return 0

    def bfs(i,j):
        queue=deque([(i,j)])
        grid[i][j]='0'

        while queue:
            x,y=queue.popleft()
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx,ny=x+dx,y+dy
                if (0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny]=='1'):
                    grid[nx][ny]='0'
                    queue.append((nx,ny))

    count=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=='1':
                count+=1
                bfs(i,j)

    return count

# 最小测试用例 - 在Python Tutor中单步调试这个
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print("BFS结果:", numIslands_simple([row[:] for row in grid]))




#########################################################
# #Python Tutor 兼容版本 (DFS)
# def numIslands(grid):
#     if not grid or not grid[0]:
#         return 0
#
#     def dfs(i,j):
#         if (i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]!='1'):
#             return
#
#         grid[i][j]='0'
#         dfs(i+1,j)
#         dfs(i-1,j)
#         dfs(i,j+1)
#         dfs(i,j-1)
#
#     count=0
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if grid[i][j]=='1':
#                 count+=1
#                 dfs(i,j)
#     return count
#
# # 测试
# grid = [
#     ["1","1","0","0","0"],
#     ["1","1","0","0","0"],
#     ["0","0","1","0","0"],
#     ["0","0","0","1","1"]
# ]
# print("岛屿数量:", numIslands([row[:] for row in grid]))
#





###############################################################################
# def numIslands_visualized(grid):
#     print("🎯 Number of Islands - DFS可视化")
#     print("=" * 60)
#     print("原始网格:")
#     for row in grid:
#         print("  " + " ".join(row))
#     print("=" * 60)
#
#     if not grid or not grid[0]:
#         print("空网格，岛屿数量: 0")
#         return 0
#
#     def dfs(i, j, island_num, depth):
#         indent = "  " * depth
#
#         print(f"{indent}↳ dfs(i={i}, j={j}) - 探索岛屿 #{island_num}")
#
#         # 边界和有效性检查
#         if (i < 0 or i >= len(grid) or
#                 j < 0 or j >= len(grid[0])):
#             print(f"{indent}  🚫 超出边界")
#             return
#
#         if grid[i][j] != '1':
#             print(f"{indent}  🚫 不是陆地: '{grid[i][j]}'")
#             return
#
#         # 标记为已访问
#         print(f"{indent}  ✅ 发现陆地，标记为已访问")
#         grid[i][j] = '0'
#
#         # 显示当前网格状态
#         print(f"{indent}  当前网格状态:")
#         for idx, row in enumerate(grid):
#             marker = ">" if idx == i else " "
#             print(f"{indent}   {marker} " + " ".join(row))
#
#         # 四个方向DFS
#         directions = [(1, 0, '下'), (-1, 0, '上'), (0, 1, '右'), (0, -1, '左')]
#         for dx, dy, direction in directions:
#             print(f"{indent}  向{direction}探索")
#             dfs(i + dx, j + dy, island_num, depth + 1)
#
#     count = 0
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if grid[i][j] == '1':
#                 count += 1
#                 print(f"\n🏝️ 发现新岛屿 #{count} 在位置 ({i},{j})")
#                 dfs(i, j, count, 0)
#
#     print(f"\n🎊 最终结果: 总共 {count} 个岛屿")
#     return count
#
#
# # 运行可视化
# print("DFS可视化演示:")
# grid = [
#     ["1", "1", "0", "0", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "1", "0", "0"],
#     ["0", "0", "0", "1", "1"]
# ]
# numIslands_visualized([row[:] for row in grid])  # 使用副本