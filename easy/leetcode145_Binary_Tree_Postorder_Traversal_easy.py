class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def postorderTraversal(self,root):
        result=[]
        self._postorder_recursive(root,result)
        return result
    def _postorder_recursive(self,node,result):
        if node is None:
            return

        self._postorder_recursive(node.left,result)
        self._postorder_recursive(node.right,result)
        result.append(node.val)