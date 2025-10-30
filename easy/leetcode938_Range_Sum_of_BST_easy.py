# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# def rangeSumBST(root, low, high):
#     """
#     Python Tutor 可验证的BST范围和方法
#     """
#
#     def dfs(node):
#         # 基准情况：空节点返回0
#         if node is None:
#             return 0
#
#         total = 0
#
#         # 检查当前节点是否在范围内
#         if low <= node.val <= high:
#             total += node.val
#
#         # 利用BST特性：如果当前值大于low，搜索左子树可能有符合条件的节点
#         if node.val > low:
#             total += dfs(node.left)
#
#         # 利用BST特性：如果当前值小于high，搜索右子树可能有符合条件的节点
#         if node.val < high:
#             total += dfs(node.right)
#
#         return total
#
#     return dfs(root)
#
#
# # 构建测试BST: [10, 5, 15, 3, 7, 18]
# #       10
# #      /  \
# #     5    15
# #    / \     \
# #   3   7     18
#
# # 创建节点
# node3 = TreeNode(3)
# node7 = TreeNode(7)
# node18 = TreeNode(18)
# node5 = TreeNode(5, node3, node7)
# node15 = TreeNode(15, None, node18)
# root = TreeNode(10, node5, node15)
#
# # 测试参数
# low = 7
# high = 15
#
# print(f"BST结构:")
# print(f"    10")
# print(f"   /  \\")
# print(f"  5    15")
# print(f" / \\     \\")
# print(f"3   7     18")
# print(f"\n计算范围 [{low}, {high}] 内的节点和")
#
# # 执行计算
# result = rangeSumBST(root, low, high)
#
# print(f"\n结果: {result}")
# print(f"验证: 在范围[{low}, {high}]内的节点有: 7, 10, 15")
# print(f"      7 + 10 + 15 = {7 + 10 + 15}")

##############################################################################
#栈
# class TreeNode:
#     def __init__(self,val=0,left=None,right=None):
#         self.val=val
#         self.left=left
#         self.right=right
#
# class Solution:
#     def rangeSumBST(self,root,low,high):
#         if not root:
#             return 0
#
#         total=0
#         stack=[root]
#
#         while stack:
#             node=stack.pop()
#
#             if low<=node.val<=high:
#                 total+=node.val
#
#             if node.left and node.val>low:
#                 stack.append(node.left)
#
#             if node.right and node.val<high:
#                 stack.append(node.right)
#         return total
#
# # 构建测试BST: [10, 5, 15, 3, 7, 18]
# #       10
# #      /  \
# #     5    15
# #    / \     \
# #   3   7     18
#
# node3 = TreeNode(3)
# node7 = TreeNode(7)
# node18 = TreeNode(18)
# node5 = TreeNode(5, node3, node7)
# node15 = TreeNode(15, None, node18)
# root = TreeNode(10, node5, node15)
#
# # 测试
# # 测试
# low, high = 7, 15
# solution = Solution()  # 创建Solution实例
# result = solution.rangeSumBST(root, low, high)  # 通过实例调用方法
#
# print(f"范围 [{low}, {high}] 内的节点和: {result}")
# print(f"验证: 7 + 10 + 15 = {7 + 10 + 15}")

######################################################################
#队列

from  collections import deque
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def rangeSumBST(self,root,low,high):
        if not root:
            return 0

        queue=deque([root])
        total=0
        while queue:
            node=queue.popleft()
            if low<=node.val<=high:
                total+=node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return total

if __name__ == "__main__":
    # 手动构造 BST：    10
    #                 /  \
    #                5   15
    #               / \    \
    #              3   7   20
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(20)

    low, high = 7, 15
    result = Solution().rangeSumBST(root, low, high)
    print(f"BST 节点值在 [{low}, {high}] 的和 = {result}")   # 预期：7+10+15 = 32
