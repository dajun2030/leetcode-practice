# class Solution:
#     def isValidBST(self, root):
#         stack=[]
#         curr=root
#         prev=None
#
#         while stack or curr:
#             while curr:
#                 stack.append(curr)
#                 curr=curr.left
#             curr=stack.pop()
#             if prev is not None and curr.val<=prev:
#                 return False
#
#             prev=curr.val
#             curr=curr.right
#         return True

#######################################################
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node, min_val, max_val):
            """
            验证以node为根的子树是否是有效的BST

            Args:
                node: 当前节点
                min_val: 当前节点允许的最小值（不包含）
                max_val: 当前节点允许的最大值（不包含）

            Returns:
                bool: 是否是有效的BST
            """
            # 空节点总是有效的
            if not node:
                return True

            # 检查当前节点值是否在合法范围内
            if node.val <= min_val or node.val >= max_val:
                return False

            # 递归验证左右子树
            # 左子树：上界变为当前节点值
            # 右子树：下界变为当前节点值
            return (validate(node.left, min_val, node.val) and
                    validate(node.right, node.val, max_val))

        # 初始调用：根节点的范围是负无穷到正无穷
        return validate(root, float('-inf'), float('inf'))


# 测试代码
def test_isValidBST():
    solution = Solution()

    # 测试用例1：有效的BST
    #     5
    #    / \
    #   3   7
    #  / \   \
    # 1   4   8
    root1 = TreeNode(5)
    root1.left = TreeNode(3)
    root1.right = TreeNode(7)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(4)
    root1.right.right = TreeNode(8)
    print("Test 1 (Valid BST):", solution.isValidBST(root1))  # 应该输出 True

    # 测试用例2：无效的BST（节点6在错误位置）
    #     5
    #    / \
    #   3   7
    #  / \   \
    # 1   6   8
    root2 = TreeNode(5)
    root2.left = TreeNode(3)
    root2.right = TreeNode(7)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(6)  # 6 > 5，违反BST规则
    root2.right.right = TreeNode(8)
    print("Test 2 (Invalid BST):", solution.isValidBST(root2))  # 应该输出 False

    # 测试用例3：单节点树
    root3 = TreeNode(1)
    print("Test 3 (Single node):", solution.isValidBST(root3))  # 应该输出 True

    # 测试用例4：空树
    root4 = None
    print("Test 4 (Empty tree):", solution.isValidBST(root4))  # 应该输出 True

    # 测试用例5：有重复值的树
    #     2
    #    / \
    #   2   3
    root5 = TreeNode(2)
    root5.left = TreeNode(2)  # 重复值，违反严格不等规则
    root5.right = TreeNode(3)
    print("Test 5 (Duplicate values):", solution.isValidBST(root5))  # 应该输出 False

    # 测试用例6：边界情况
    #   2147483647
    root6 = TreeNode(2147483647)
    print("Test 6 (Max int):", solution.isValidBST(root6))  # 应该输出 True


if __name__ == "__main__":
    test_isValidBST()