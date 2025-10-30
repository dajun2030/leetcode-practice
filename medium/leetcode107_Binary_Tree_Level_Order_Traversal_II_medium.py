# LeetCode 107. Binary Tree Level Order Traversal II
# 给定一个二叉树，返回其节点值自底向上的层序遍历。（即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> list[list[int]]:
        # 处理空树情况
        if not root:
            return []

        # 使用队列进行层序遍历
        queue = [root]
        result = []

        # 层序遍历
        while queue:
            # 当前层的节点数量
            level_size = len(queue)
            # 存储当前层的节点值
            current_level = []

            # 遍历当前层的所有节点
            for _ in range(level_size):
                # 取出队首节点
                node = queue.pop(0)
                # 将节点值加入当前层列表
                current_level.append(node.val)

                # 将子节点加入队列，准备下一层遍历
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # 将当前层结果加入总结果
            result.append(current_level)

        # 反转结果，实现自底向上
        return result[::-1]


# 测试用例
def build_tree(nodes):
    """
    根据层序遍历数组构建二叉树
    None表示空节点
    """
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = [root]
    i = 1

    while queue and i < len(nodes):
        node = queue.pop(0)

        # 左子节点
        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1

        # 右子节点
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1

    return root


# 测试用例
def run_tests():
    # 测试用例1: [3,9,20,None,None,15,7]
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    test1 = build_tree([3, 9, 20, None, None, 15, 7])

    # 测试用例2: [1]
    test2 = build_tree([1])

    # 测试用例3: []
    test3 = build_tree([])

    # 测试用例4: [1,2,3,4,5]
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    test4 = build_tree([1, 2, 3, 4, 5])

    solution = Solution()

    print("测试用例1结果:")
    print(solution.levelOrderBottom(test1))  # 预期输出: [[15, 7], [9, 20], [3]]

    print("\n测试用例2结果:")
    print(solution.levelOrderBottom(test2))  # 预期输出: [[1]]

    print("\n测试用例3结果:")
    print(solution.levelOrderBottom(test3))  # 预期输出: []

    print("\n测试用例4结果:")
    print(solution.levelOrderBottom(test4))  # 预期输出: [[4, 5], [2, 3], [1]]


if __name__ == "__main__":
    run_tests()