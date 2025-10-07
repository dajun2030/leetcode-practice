# #后序遍历
# class Solution:
#     def isBalanced(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#
#         # 第1行：定义内部检查函数
#         def check(node):
#             # 第2行：递归终止条件 - 空节点
#             if not node:
#                 return 0
#
#             # 第3行：递归检查左子树
#             left = check(node.left)
#
#             # 第4行：如果左子树不平衡，直接返回-1
#             if left == -1:
#                 return -1
#
#             # 第5行：递归检查右子树
#             right = check(node.right)
#
#             # 第6行：如果右子树不平衡，直接返回-1
#             if right == -1:
#                 return -1
#
#             # 第7行：检查当前节点是否平衡
#             if abs(left - right) > 1:
#                 return -1
#
#             # 第8行：返回当前节点的高度
#             return max(left, right) + 1
#
#         # 第9行：启动检查，结果不是-1就表示平衡
#         return check(root) != -1

############################################################

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def check(node):
            # 第1行：递归终止条件
            if not node:
                print(f"    🎯 空节点 → 返回高度 0")
                return 0

            print(f"  🔍 进入节点 {node.val}")

            # 第2行：递归检查左子树
            print(f"    ← 检查左子树...")
            left = check(node.left)

            # 第3行：如果左子树不平衡，直接返回-1
            if left == -1:
                print(f"    ❌ 节点 {node.val} 的左子树不平衡，提前返回 -1")
                return -1

            # 第4行：递归检查右子树
            print(f"    → 检查右子树...")
            right = check(node.right)

            # 第5行：如果右子树不平衡，直接返回-1
            if right == -1:
                print(f"    ❌ 节点 {node.val} 的右子树不平衡，提前返回 -1")
                return -1

            # 第6行：检查当前节点是否平衡
            print(f"    📊 节点 {node.val}: 左高度={left}, 右高度={right}, 高度差={abs(left - right)}")
            if abs(left - right) > 1:
                print(f"    ❌ 节点 {node.val} 不平衡! |{left}-{right}|={abs(left - right)} > 1")
                return -1

            # 第7行：返回当前节点的高度
            height = max(left, right) + 1
            print(f"    ✅ 节点 {node.val} 平衡 → 返回高度 {height}")
            return height

        print(f"🌳 开始检查平衡性...")
        result = check(root)
        print(f"🎯 最终结果: {result != -1} (check返回{result})")
        return result != -1


def build_tree(values):
    """根据层次遍历列表构建二叉树"""
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


def print_tree(root, level=0, prefix="Root: "):
    """可视化打印树结构"""
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left is not None or root.right is not None:
            if root.left:
                print_tree(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if root.right:
                print_tree(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")


# 测试用例
def test_balanced_tree():
    print("=" * 60)
    print("测试用例1: 平衡二叉树")
    print("=" * 60)

    # 构建平衡树: [3,9,20,null,null,15,7]
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    values = [3, 9, 20, None, None, 15, 7]
    tree = build_tree(values)

    print("树结构:")
    print_tree(tree)
    print()

    solution = Solution()
    result = solution.isBalanced(tree)

    print(f"\n📋 测试结果: {result} (期望: True)")
    print(f"✅ {'通过' if result == True else '失败'}")
    return result


def test_unbalanced_tree():
    print("\n" + "=" * 60)
    print("测试用例2: 不平衡二叉树")
    print("=" * 60)

    # 构建不平衡树: [1,2,2,3,3,null,null,4,4]
    #        1
    #       / \
    #      2   2
    #     / \
    #    3   3
    #   / \
    #  4   4
    values = [1, 2, 2, 3, 3, None, None, 4, 4]
    tree = build_tree(values)

    print("树结构:")
    print_tree(tree)
    print()

    solution = Solution()
    result = solution.isBalanced(tree)

    print(f"\n📋 测试结果: {result} (期望: False)")
    print(f"✅ {'通过' if result == False else '失败'}")
    return result


def test_single_node():
    print("\n" + "=" * 60)
    print("测试用例3: 单节点树")
    print("=" * 60)

    values = [1]
    tree = build_tree(values)

    print("树结构:")
    print_tree(tree)
    print()

    solution = Solution()
    result = solution.isBalanced(tree)

    print(f"\n📋 测试结果: {result} (期望: True)")
    print(f"✅ {'通过' if result == True else '失败'}")
    return result


def test_empty_tree():
    print("\n" + "=" * 60)
    print("测试用例4: 空树")
    print("=" * 60)

    tree = None

    print("树结构: 空树")
    print()

    solution = Solution()
    result = solution.isBalanced(tree)

    print(f"\n📋 测试结果: {result} (期望: True)")
    print(f"✅ {'通过' if result == True else '失败'}")
    return result


def test_left_heavy():
    print("\n" + "=" * 60)
    print("测试用例5: 左重树")
    print("=" * 60)

    # 左子树比右子树深2层
    #     1
    #    / \
    #   2   3
    #  /
    # 4
    values = [1, 2, 3, 4]
    tree = build_tree(values)

    print("树结构:")
    print_tree(tree)
    print()

    solution = Solution()
    result = solution.isBalanced(tree)

    print(f"\n📋 测试结果: {result} (期望: True)")  # |2-1|=1，仍然平衡
    print(f"✅ {'通过' if result == True else '失败'}")
    return result


# 运行所有测试
if __name__ == "__main__":
    print("平衡二叉树验证测试")
    print("=" * 60)

    test_cases = [
        test_balanced_tree,
        test_unbalanced_tree,
        test_single_node,
        test_empty_tree,
        test_left_heavy
    ]

    passed = 0
    for test_case in test_cases:
        if test_case():
            passed += 1

    print("\n" + "=" * 60)
    print(f"🎉 测试总结: {passed}/{len(test_cases)} 通过")
    print("=" * 60)