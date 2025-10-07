# def isSymmetric(self, root):
#     if not root:
#         return True
#
#     def isMirror(left,right):
#         if not left and not right:
#             return True
#         if not left or not right:
#             return False
#         if left.val !=right.val:
#             return False
#
#         return isMirror(left.left,right.right) and isMirror(left.right,right.left)
#     return isMirror(root.left,root.right)
###############################################################################

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 第1行：处理空树情况
        if not root:
            print("    ✅ 空树 → 返回 True")
            return True

        print(f"🌳 开始检查树是否对称，根节点: {root.val}")

        # 第2行：定义内部镜像比较函数
        def isMirror(left, right):
            # 第3行：两个节点都为空
            if not left and not right:
                print(f"        ✅ 两个节点都为空 → 返回 True")
                return True

            # 第4行：一个节点为空，另一个不为空
            if not left or not right:
                left_val = left.val if left else "None"
                right_val = right.val if right else "None"
                print(f"        ❌ 结构不对称: left={left_val}, right={right_val} → 返回 False")
                return False

            # 第5行：节点值不相等
            if left.val != right.val:
                print(f"        ❌ 值不对称: left.val={left.val}, right.val={right.val} → 返回 False")
                return False

            print(f"        🔍 节点 left={left.val}, right={right.val} 相同，继续检查子树...")

            # 第6行：递归比较镜像位置
            outer_match = isMirror(left.left, right.right)  # 外层比较
            inner_match = isMirror(left.right, right.left)  # 内层比较

            result = outer_match and inner_match
            print(
                f"        📊 节点 {left.val}: 外层{'对称' if outer_match else '不对称'}, 内层{'对称' if inner_match else '不对称'} → {result}")

            return result

        # 第7行：启动镜像比较
        print(f"    🔍 比较左右子树...")
        result = isMirror(root.left, root.right)
        print(f"🎯 最终结果: {result}")
        return result


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
    print("测试用例1: 对称树 [1,2,2,3,4,4,3]")
    print("=" * 70)

    # 构建对称树:
    #     1
    #    / \
    #   2   2
    #  / \ / \
    # 3  4 4  3
    values = [1, 2, 2, 3, 4, 4, 3]
    tree = build_tree(values)

    print("树结构:")
    print_tree(tree)
    print("\n检查过程:")

    solution = Solution()
    result = solution.isSymmetric(tree)

    print(f"\n📋 测试结果: {result} (期望: True)")
    print(f"✅ {'通过' if result == True else '失败'}")
    return result == True


def test_case_2():
    print("\n" + "=" * 70)
    print("测试用例2: 不对称树 [1,2,2,null,3,null,3]")
    print("=" * 70)

    # 构建不对称树:
    #     1
    #    / \
    #   2   2
    #    \   \
    #    3    3
    values = [1, 2, 2, None, 3, None, 3]
    tree = build_tree(values)

    print("树结构:")
    print_tree(tree)
    print("\n检查过程:")

    solution = Solution()
    result = solution.isSymmetric(tree)

    print(f"\n📋 测试结果: {result} (期望: False)")
    print(f"✅ {'通过' if result == False else '失败'}")
    return result == False


def test_case_3():
    print("\n" + "=" * 70)
    print("测试用例3: 单节点树 [1]")
    print("=" * 70)

    values = [1]
    tree = build_tree(values)

    print("树结构:")
    print_tree(tree)
    print("\n检查过程:")

    solution = Solution()
    result = solution.isSymmetric(tree)

    print(f"\n📋 测试结果: {result} (期望: True)")
    print(f"✅ {'通过' if result == True else '失败'}")
    return result == True


def test_case_4():
    print("\n" + "=" * 70)
    print("测试用例4: 空树")
    print("=" * 70)

    tree = None

    print("树结构: 空树")
    print("\n检查过程:")

    solution = Solution()
    result = solution.isSymmetric(tree)

    print(f"\n📋 测试结果: {result} (期望: True)")
    print(f"✅ {'通过' if result == True else '失败'}")
    return result == True


def test_case_5():
    print("\n" + "=" * 70)
    print("测试用例5: 值不对称树 [1,2,2,3,4,3,4]")
    print("=" * 70)

    # 构建值不对称树:
    #     1
    #    / \
    #   2   2
    #  / \ / \
    # 3  4 3  4  (注意这里的值不对称)
    values = [1, 2, 2, 3, 4, 3, 4]
    tree = build_tree(values)

    print("树结构:")
    print_tree(tree)
    print("\n检查过程:")

    solution = Solution()
    result = solution.isSymmetric(tree)

    print(f"\n📋 测试结果: {result} (期望: False)")
    print(f"✅ {'通过' if result == False else '失败'}")
    return result == False


def test_case_6():
    print("\n" + "=" * 70)
    print("测试用例6: 复杂对称树 [1,2,2,3,4,4,3,5,6,7,8,8,7,6,5]")
    print("=" * 70)

    # 构建复杂对称树:
    #           1
    #        /     \
    #       2       2
    #      / \     / \
    #     3   4   4   3
    #    / \ / \ / \ / \
    #   5  6 7 8 8 7 6 5
    values = [1, 2, 2, 3, 4, 4, 3, 5, 6, 7, 8, 8, 7, 6, 5]
    tree = build_tree(values)

    print("树结构:")
    print_tree(tree)
    print("\n检查过程:")

    solution = Solution()
    result = solution.isSymmetric(tree)

    print(f"\n📋 测试结果: {result} (期望: True)")
    print(f"✅ {'通过' if result == True else '失败'}")
    return result == True


def test_case_7():
    print("\n" + "=" * 70)
    print("测试用例7: 只有左子树 [1,2]")
    print("=" * 70)

    values = [1, 2]
    tree = build_tree(values)

    print("树结构:")
    print_tree(tree)
    print("\n检查过程:")

    solution = Solution()
    result = solution.isSymmetric(tree)

    print(f"\n📋 测试结果: {result} (期望: False)")
    print(f"✅ {'通过' if result == False else '失败'}")
    return result == False


# 运行所有测试
if __name__ == "__main__":
    print("对称二叉树验证测试")
    print("=" * 70)

    test_cases = [
        test_case_1,  # 对称树
        test_case_2,  # 不对称树（结构）
        test_case_3,  # 单节点
        test_case_4,  # 空树
        test_case_5,  # 值不对称
        test_case_6,  # 复杂对称
        test_case_7  # 只有左子树
    ]

    passed = 0
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n🚀 运行测试用例 {i}...")
        if test_case():
            passed += 1

    print("\n" + "=" * 70)
    print(f"🎉 测试总结: {passed}/{len(test_cases)} 通过")
    print("=" * 70)

    # 显示算法逻辑总结
    print("\n💡 镜像对称算法逻辑:")
    print("1. ✅ 两个节点都为空 → 对称")
    print("2. ❌ 一个为空一个不为空 → 不对称")
    print("3. ❌ 节点值不相等 → 不对称")
    print("4. 🔍 递归检查:")
    print("   - 左树的左子树 ↔ 右树的右子树 (外层)")
    print("   - 左树的右子树 ↔ 右树的左子树 (内层)")