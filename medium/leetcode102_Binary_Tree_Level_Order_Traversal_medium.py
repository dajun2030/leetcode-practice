# from collections import deque
# class TreeNode:
#     def __init__(self,val=0,left=None,right=None):
#         self.val=val
#         self.left=left
#         self.right=right
#
# class Solution:
#     def levelOrder(self, root):
#         if not root:
#             return []
#
#         result=[]
#         queue=deque([root])
#         while queue:
#             level_size=len(queue)
#             current_level=[]
#             for _ in range(level_size):
#                 node=queue.popleft()
#                 current_level.append(node.val)
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             result.append( current_level)
#         return result
#
#
# def main():
#     # 构建示例树: [3,9,20,null,null,15,7]
#     #     3
#     #    / \
#     #   9  20
#     #     /  \
#     #    15   7
#
#     root = TreeNode(3)
#     root.left = TreeNode(9)
#     root.right = TreeNode(20)
#     root.right.left = TreeNode(15)
#     root.right.right = TreeNode(7)
#
#     solution = Solution()
#     result = solution.levelOrder(root)
#     print("层序遍历结果:", result)
#     # 输出: [[3], [9, 20], [15, 7]]
#
#
# if __name__ == "__main__":
#     main()

############################################
#DFS
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        result = []

        def dfs(node, level):
            if not node:
                return

            # 如果当前层还没有列表，创建一个
            if len(result) == level:
                result.append([])

            # 将节点值添加到对应层
            result[level].append(node.val)

            # 递归遍历左右子树
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return result


# 测试
def main():
    # 构建树: [3,9,20,null,null,15,7]
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()
    print("DFS层序遍历:", solution.levelOrder(root))
    # 输出: [[3], [9, 20], [15, 7]]


if __name__ == "__main__":
    main()