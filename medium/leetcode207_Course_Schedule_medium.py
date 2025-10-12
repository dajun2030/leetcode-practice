from collections import deque,defaultdict

def canFinish(numCourses,prerequisites):
    #构建图和入度数组
    graph=defaultdict(list)
    indegree=[0]*numCourses

    #构建依赖关系
    for course,prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course]+=1

    #初始化队列
    queue=deque()
    for i in range(numCourses):
        if indegree[i]==0:
            queue.append(i)

    #拓扑排序
    count=0
    while queue:
        current=queue.popleft()
        count+=1

        #处理后继课程
        for neighbor in graph[current]:
            indegree[neighbor]-=1
            if indegree[neighbor]==0:
                queue.append(neighbor)
    return count==numCourses