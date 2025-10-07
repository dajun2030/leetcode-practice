# class Solution:
#     def diameterOfBinaryTree(self, root):
#         self.diameter=0
#
#         def depth(node):
#             if not node:
#                 return 0
#
#             left_depth=depth(node.left)
#             right_depth=depth(node.right)
#
#             self.diameter=max(self.diameter,left_depth+right_depth)
#
#             return max(left_depth,right_depth)+1
#         depth(root)
#         return self.diameter

################################################################

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = 0

        def depth(node):
            if not node:
                print(f"      🎯 空节点 → 返回深度 0")
                return 0

            print(f"  🔍 访问节点 {node.val}")

            # 递归获取左右子树深度
            print(f"    ← 计算左子树深度...")
            left_depth = depth(node.left)
            print(f"    → 计算右子树深度...")
            right_depth = depth(node.right)

            # 计算经过当前节点的路径长度
            path_through_node = left_depth + right_depth
            print(f"    📏 节点 {node.val}: 左深度={left_depth}, 右深度={right_depth}, 路径长度={path_through_node}")

            # 更新全局直径
            if path_through_node > self.diameter:
                print(f"    🎯 更新直径: {self.diameter} → {path_through_node}")
                self.diameter = path_through_node
            else:
                print(f"    📊 当前直径保持: {self.diameter}")

            # 返回当前节点深度
            current_depth = max(left_depth, right_depth) + 1
            print(f"    📐 节点 {node.val} 深度: max({left_depth},{right_depth})+1 = {current_depth}")
            return current_depth

        print(f"🌳 开始计算二叉树直径...")
        depth(root)
        print(f"🎯 最终直径: {self.diameter}")
        return self.diameter


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
def test_case_1():
    print("=" * 70)
    print("测试用例1: 经典示例 [1,2,3,4,5]")
    print("=" * 70)

    # 构建树:
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    values = [1, 2, 3, 4, 5]
    tree = build_tree(values)

    print("树结构:")
    print_tree(tree)
    print("\n计算过程:")

    solution = Solution()
    result = solution.diameterOfBinaryTree(tree)

    print(f"\n📋 测试结果: 直径 = {result} (期望: 3)")
    print(f"✅ {'通过' if result == 3 else '失败'}")
    return result == 3


def test_case_2():
    print("\n" + "=" * 70)
    print("测试用例2: 单边树 [1,2,null,3,null,4,null,5]")
    print("=" * 70)

    # 构建树:
    #     1
    #    /
    #   2
    #  /
    # 3
    #  \
    #   4
    #    \
    #     5
    values = [1, 2, None, 3, None, 4, None, 5]
    tree = build_tree(values)

    print("树结构:")
    print_tree(tree)
    print("\n计算过程:")

    solution = Solution()
    result = solution.diameterOfBinaryTree(tree)

    print(f"\n📋 测试结果: 直径 = {result} (期望: 4)")
    print(f"✅ {'通过' if result == 4 else '失败'}")
    return result == 4


def test_case_3():
    print("\n" + "=" * 70)
    print("测试用例3: 复杂不平衡树 [1,2,3,4,5,null,null,6,7,8,9]")
    print("=" * 70)

    # 构建树:
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5
    #   /   /
    #  6   7
    #     / \
    #    8   9
    values = [1, 2, 3, 4, 5, None, None, 6, 7, 8, 9]
    tree = build_tree(values)

    print("树结构:")
    print_tree(tree)
    print("\n计算过程:")

    solution = Solution()
    result = solution.diameterOfBinaryTree(tree)

    print(f"\n📋 测试结果: 直径 = {result} (期望: 5)")
    print(f"✅ {'通过' if result == 5 else '失败'}")
    return result == 5


def test_case_4():
    print("\n" + "=" * 70)
    print("测试用例4: 单节点树 [1]")
    print("=" * 70)

    values = [1]
    tree = build_tree(values)

    print("树结构:")
    print_tree(tree)
    print("\n计算过程:")

    solution = Solution()
    result = solution.diameterOfBinaryTree(tree)

    print(f"\n📋 测试结果: 直径 = {result} (期望: 0)")
    print(f"✅ {'通过' if result == 0 else '失败'}")
    return result == 0


def test_case_5():
    print("\n" + "=" * 70)
    print("测试用例5: 空树")
    print("=" * 70)

    tree = None

    print("树结构: 空树")
    print("\n计算过程:")

    solution = Solution()
    result = solution.diameterOfBinaryTree(tree)

    print(f"\n📋 测试结果: 直径 = {result} (期望: 0)")
    print(f"✅ {'通过' if result == 0 else '失败'}")
    return result == 0


def test_case_6():
    print("\n" + "=" * 70)
    print("测试用例6: 直径不经过根节点 [1,2,3,4,null,null,5,6,null,7]")
    print("=" * 70)

    # 构建树:
    #        1
    #       / \
    #      2   3
    #     /     \
    #    4       5
    #   /       /
    #  6       7
    values = [1, 2, 3, 4, None, None, 5, 6, None, 7]
    tree = build_tree(values)

    print("树结构:")
    print_tree(tree)
    print("\n计算过程:")

    solution = Solution()
    result = solution.diameterOfBinaryTree(tree)

    print(f"\n📋 测试结果: 直径 = {result} (期望: 5)")
    print(f"✅ {'通过' if result == 5 else '失败'}")
    return result == 5


# 运行所有测试
if __name__ == "__main__":
    print("二叉树直径计算验证测试")
    print("=" * 70)

    test_cases = [
        test_case_1,  # 经典示例
        test_case_2,  # 单边树
        test_case_3,  # 复杂树
        test_case_4,  # 单节点
        test_case_5,  # 空树
        test_case_6  # 直径不经过根节点
    ]

    passed = 0
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n🚀 运行测试用例 {i}...")
        if test_case():
            passed += 1

    print("\n" + "=" * 70)
    print(f"🎉 测试总结: {passed}/{len(test_cases)} 通过")
    print("=" * 70)

    # 额外验证：显示关键洞察
    print("\n💡 关键洞察:")
    print("• 直径 = 所有节点中 (左深度 + 右深度) 的最大值")
    print("• 直径可能不经过根节点")
    print("• 单节点树的直径为0（没有边）")
    print("• 空树的直径为0")