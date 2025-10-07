#1.递归法
#class Solution:
#     def invertTree(self, root):
#         if not root:
#             return root
#
#         root.left,root.right=root.right,root.left
#
#         self.invertTree(root.left)
#         self.invertTree(root.right)
#
#         return root

#2 迭代法
from collections import deque
def invertTree(root):
    if not root:
        return root

    queue=deque([root])
    while queue:
        node=queue.popleft()
        node.left,node.right=node.right,node.left

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return root