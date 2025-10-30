#递归解法
class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def isSymmetric(root):
        if not root:
            return True

        def isMirror(left,right):
            if not left and not right:
                return True

            if not left or not right:
                return False

            if left.val!=right.val:
                return False

            return isMirror(left.left,right.right) and isMirror(left.right,right.left)
        return isMirror(root.left,root.right)

####################################################
#DFS解法

def isSymmetric(root):
    if not root:
        return True

    stack=[]
    stack.append((root.left,root.right))
    while stack:
        left,right=stack.pop()
        if not left and not right:
            continue

        if not left or not right:
            return False

        if left.val!=right.val:
            return False

        stack.append((left.right,right.left))
        stack.append((left.left,right.right))

    return True

########################################################
#BFS
from collections import deque
def isSymmetric(root):
    if not root:
        return True

    queue=deque()
    queue.append((root.left,root.right))
    while queue:
        left,right=queue.popleft()
        if not left and not right:
            continue

        if not left or not right:
            return False

        if left.val!=right.val:
            return False

        queue.append((left.left, right.right))
        queue.append((left.right,right.left))

    return True