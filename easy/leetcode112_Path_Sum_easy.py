class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        if not root.left and not root.right:
            return root.val==targetSum

        remaining=targetSum-root.val

        return self.hasPathSum(root.left,remaining) or self.hasPathSum(root.right,remaining)