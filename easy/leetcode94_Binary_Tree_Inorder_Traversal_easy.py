class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def inorderTraversal(self,root):
        result=[]
        self._inorder_recursive(root,result)
        return result
    def _inorder_recursive(self,node,result):
        if node is None:
            return

        self._inorder_recursive(node.left,result)
        result.append(node.val)
        self._inorder_recursive(node.right,result)