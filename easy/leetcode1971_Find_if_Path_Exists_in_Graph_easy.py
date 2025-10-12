from collections import deque, defaultdict

def validPath(n, edges, source, destination):
    # 构建邻接表
    graph=defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)

    #BFS
    visited=set()
    queue=deque([source])
    visited.add(source)

    while queue:
        node=queue.popleft()

        if node==destination:
            return True

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return False