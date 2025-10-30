#递归
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def preorderTraversal(self,root):
        result=[]
        self._preorder_recursive(root,result)
        return result

    def _preorder_recursive(self,node,result):
        if node is None:
            return

        result.append(node.val)
        self._preorder_recursive(node.left,result)
        self._preorder_recursive(node.right,result)

##################################################################
class Solution:
    def preorderTraversal(self, root):
        """
        迭代实现的模板写法
        更通用的二叉树遍历写法
        """
        if not root:
            return []

        result = []
        stack = []
        current = root

        while current or stack:
            # 一路向左，访问所有节点
            while current:
                result.append(current.val)  # 访问当前节点
                stack.append(current)  # 将节点入栈，用于后续访问右子树
                current = current.left  # 移动到左子节点

            # 当左子树遍历完毕，弹出栈顶节点，处理右子树
            current = stack.pop()
            current = current.right

        return result
#
# #####################################################################
# #morris
# class Solution:
#     def preorderTraversal(self, root):
#         """
#         Morris前序遍历 - 常数空间复杂度
#         通过修改树的结构（临时）来实现遍历
#         """
#         result = []
#         current = root
#
#         while current:
#             if not current.left:
#                 # 如果没有左子节点，访问当前节点并转向右子树
#                 result.append(current.val)
#                 current = current.right
#             else:
#                 # 找到当前节点的前驱节点（左子树的最右节点）
#                 predecessor = current.left
#                 while predecessor.right and predecessor.right != current:
#                     predecessor = predecessor.right
#
#                 if not predecessor.right:
#                     # 第一次访问当前节点，建立临时链接
#                     result.append(current.val)  # 访问当前节点
#                     predecessor.right = current  # 建立临时链接
#                     current = current.left  # 转向左子树
#                 else:
#                     # 第二次访问当前节点，恢复树结构
#                     predecessor.right = None  # 删除临时链接
#                     current = current.right  # 转向右子树
#
#         return result

##################################################################

def test_preorder_traversal():
    """测试前序遍历的各种实现"""

    # 构建测试二叉树: [1,2,3,4,5]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()

    # 测试递归实现
    result_recursive = solution.preorderTraversal(root)
    print(f"递归前序遍历: {result_recursive}")  # [1, 2, 4, 5, 3]

    # 测试迭代实现
    result_iterative = solution.preorderTraversal(root)
    print(f"迭代前序遍历: {result_iterative}")  # [1, 2, 4, 5, 3]

    # 测试边界情况
    print(f"空树: {solution.preorderTraversal(None)}")  # []

    # 单节点树
    single_node = TreeNode(1)
    print(f"单节点树: {solution.preorderTraversal(single_node)}")  # [1]


# 运行测试
test_preorder_traversal()