from collections import deque
def orangesRotting(grid):
    if not grid or not grid[0]:
        return 0

    m=len(grid)
    n=len(grid[0])
    queue=deque()
    fresh_count=0

    #初始化
    for i in range(m):
        for j in range(n):
            if grid[i][j]==2:
                queue.append((i,j,0))
            elif grid[i][j]==1:
                fresh_count+=1

    if fresh_count==0:
        return 0

    directions=[(1,0),(0,1),(-1,0),(0,-1)]
    minutes=0
    while queue:
        x,y,time=queue.popleft()
        minutes=time

        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<m and 0<=ny<n and grid[nx][ny]==1:
                grid[nx][ny]=2
                fresh_count-=1
                queue.append((nx,ny,time+1))
    return minutes if fresh_count==0 else -1

# Python Tutor 测试
def test_python_tutor():
    grid = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]
    result = orangesRotting(grid)
    print("结果:", result)
    return result

# 复制到 Python Tutor 运行
test_python_tutor()

