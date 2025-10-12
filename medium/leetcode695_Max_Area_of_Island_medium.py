# def maxAreaOfIsland(grid):
#     if not grid or not grid[0]:
#         return 0
#
#     def dfs(i,j):
#         if (i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]!=1):
#             return 0
#
#         grid[i][j]=0
#
#         area=1
#         area+=dfs(i+1,j)
#         area+=dfs(i-1,j)
#         area+=dfs(i,j+1)
#         area+=dfs(i,j-1)
#
#         return area
#
#     max_area=0
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if grid[i][j]==1:
#                 current_area=dfs(i,j)
#                 if current_area>max_area:
#                     max_area=current_area
#     return max_area
#
#
# # 测试
# grid = [
#     [1, 1, 0, 0, 0],
#     [1, 1, 0, 0, 0],
#     [0, 0, 0, 1, 1],
#     [0, 0, 0, 1, 1]
# ]
# print("最大岛屿面积:", maxAreaOfIsland([row[:] for row in grid]))
#
############################################################
#bfs
from collections import deque

def maxAreaOfIsland(grid):
    if not grid or not grid[0]:
        return 0

    rows=len(grid)
    cols=len(grid[0])
    max_area=0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j]==1:
                area=0
                queue=deque([(i,j)])
                grid[i][j]=0
                area+=1

                while queue:
                    x,y=queue.popleft()
                    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==1:
                            grid[nx][ny]=0
                            area+=1
                            queue.append((nx,ny))

                if area>max_area:
                    max_area=area
    return max_area

# 在Python Tutor中单步执行这个
test_grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1]
]

print("Python Tutor单步测试:")
print("原始网格:")
for row in test_grid:
    print("  " + " ".join(map(str, row)))

result = maxAreaOfIsland([row[:] for row in test_grid])
print("最大岛屿面积:", result)
print("期望: 4")

