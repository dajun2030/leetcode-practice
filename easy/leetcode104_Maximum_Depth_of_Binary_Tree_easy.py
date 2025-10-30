
def maxDepth(root):
    if not root:
        return 0

    left_depth=maxDepth(root.left)
    right_depth=maxDepth(root.right)
    return max(left_depth, right_depth) + 1

from binarytree import build

# 一行代码构建树
values = [3, 9, 20, None, None, 15, 7]
tree = build(values)
print(tree)  # 自动可视化打印

# 直接使用
depth = maxDepth(tree)
print(depth)

#############################################################
#BFS
from collections import deque
def maxDepth(root):
    if not root:
        return 0

    queue=deque([root])

    depth=0
    while queue:
        level_size=len(queue)
        for i in range(level_size):
            node =queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        depth+=1

    return depth
#######################################################
#DFS
def maxDepth(root):
    if not root:
        return 0

    stack=[(root,1)]
    max_depth=0
    while stack:
        node,depth=stack.pop()
        max_depth=max(max_depth,depth)

        if node.right:
            stack.append((node.right,depth+1))
        if node.left:
            stack.append((node.left,depth+1))

    return max_depth