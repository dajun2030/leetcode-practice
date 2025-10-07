# from collections import deque
#
# class Solution:
#     def averageOfLevels(self, root):
#         if not root:
#             return []
#
#         result=[]
#         queue=deque([root])
#
#         while queue:
#             level_size=len(queue)
#             level_sum=0
#             for _ in range(level_size):
#                 node=queue.popleft()
#                 level_sum+=node.val
#
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             result.append(float(level_sum)/level_size)
#         return result
##################################################################

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_sum = 0

            print(f"处理第{len(result)}层，节点数: {level_size}")

            for i in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                print(f"  处理节点 {node.val}, 当前总和: {level_sum}")

                if node.left:
                    queue.append(node.left)
                    print(f"    加入左子节点 {node.left.val}")
                if node.right:
                    queue.append(node.right)
                    print(f"    加入右子节点 {node.right.val}")

            average = level_sum / level_size
            print(f"第{len(result)}层平均值: {level_sum} / {level_size} = {average}")
            result.append(average)
            print(f"当前结果: {result}\n")

        return result


# 测试代码
def test_solution():
    # 构建测试树: [3,9,20,15,7]
    #     3
    #    / \
    #   9  20
    #  / \
    # 15  7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = TreeNode(15)
    root.left.right = TreeNode(7)

    print("测试树结构:")
    print("    3")
    print("   / \\")
    print("  9  20")
    print(" / \\")
    print("15  7")
    print("\n计算过程:")

    solution = Solution()
    result = solution.averageOfLevels(root)

    print(f"最终结果: {result}")
    print(f"期望结果: [3.0, 14.5, 11.0]")
    print(f"测试: {'通过' if result == [3.0, 14.5, 11.0] else '失败'}")


# 运行测试
if __name__ == "__main__":
    test_solution()
