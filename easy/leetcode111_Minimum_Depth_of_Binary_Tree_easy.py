class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

#BFS
from collections import deque
class Solution:
    def minDepth(self,root):
        if not root:
            return 0

        queue=deque()
        queue.append((root,1))
        while queue:
            node,depth=queue.popleft()
            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append((node.left,depth+1))
            if node.right:
                queue.append((node.right,depth+1))
        return 0

#DFS
def minDepth(root):
    if not root:
        return 0

    stack=[]
    stack.append((root,1))
    min_depth=float('inf')
    while stack:
        node,depth=stack.pop()
        if not node.left and not node.right:
            min_depth=min(min_depth,depth)

        if node.right:
            stack.append((node.right,depth+1))
        if node.left:
            stack.append((node.left,depth+1))

    return min_depth

##########################
#DFS递归解法
class Solution:
    def minDepth(self,root):
        if not root:
            return 0

        if not root.left:
            return self.minDepth(root.right)+1
        if not root.right:
            return self.minDepth(root.left)+1

        return min(self.minDepth(root.left),self.minDepth(root.right))+1

