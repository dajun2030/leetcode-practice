class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        # 空子树情况
        if not subRoot:
            print(f"    ✅ 子树为空 → 返回 True")
            return True
        # 主树为空但子树不为空
        if not root:
            print(f"    ❌ 主树为空但子树不为空 → 返回 False")
            return False

        print(f"🔍 检查主树节点 {root.val} 是否包含子树 {subRoot.val}")

        # 检查当前节点开始的子树是否匹配
        if self.isSameTree(root, subRoot):
            print(f"    🎉 节点 {root.val} 开始的子树匹配!")
            return True

        # 递归检查左右子树
        print(f"    🧭 继续在左右子树中寻找...")
        left_result = self.isSubtree(root.left, subRoot) if root.left else False
        right_result = self.isSubtree(root.right, subRoot) if root.right else False

        result = left_result or right_result
        print(
            f"    📊 节点 {root.val}: 左子树{'找到' if left_result else '未找到'} 或 右子树{'找到' if right_result else '未找到'} → {result}")

        return result

    def isSameTree(self, p, q):
        """
        检查两棵树是否完全相同
        """
        # 都为空
        if not p and not q:
            return True
        # 一个为空一个不为空
        if not p or not q:
            return False
        # 值不相等
        if p.val != q.val:
            return False
        # 递归比较左右子树
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


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
    print("测试用例1: 经典示例 - 包含子树")
    print("=" * 70)

    # 构建主树: [3,4,5,1,2]
    #    3
    #   / \
    #  4   5
    # / \
    # 1   2
    root_values = [3, 4, 5, 1, 2]

    # 构建子树: [4,1,2]
    #    4
    #   / \
    #  1   2
    subRoot_values = [4, 1, 2]

    root = build_tree(root_values)
    subRoot = build_tree(subRoot_values)

    print("主树结构:")
    print_tree(root)
    print("\n子树结构:")
    print_tree(subRoot)
    print("\n搜索过程:")

    solution = Solution()
    result = solution.isSubtree(root, subRoot)

    print(f"\n📋 测试结果: {result} (期望: True)")
    print(f"✅ {'通过' if result == True else '失败'}")
    return result == True


def test_case_2():
    print("\n" + "=" * 70)
    print("测试用例2: 不包含子树")
    print("=" * 70)

    # 构建主树: [3,4,5,1,2,null,null,null,null,0]
    #    3
    #   / \
    #  4   5
    # / \
    # 1   2
    #   /
    #  0
    root_values = [3, 4, 5, 1, 2, None, None, None, None, 0]

    # 构建子树: [4,1,2]
    #    4
    #   / \
    #  1   2
    subRoot_values = [4, 1, 2]

    root = build_tree(root_values)
    subRoot = build_tree(subRoot_values)

    print("主树结构:")
    print_tree(root)
    print("\n子树结构:")
    print_tree(subRoot)
    print("\n搜索过程:")

    solution = Solution()
    result = solution.isSubtree(root, subRoot)

    print(f"\n📋 测试结果: {result} (期望: False)")
    print(f"✅ {'通过' if result == False else '失败'}")
    return result == False


def test_case_3():
    print("\n" + "=" * 70)
    print("测试用例3: 子树就是主树本身")
    print("=" * 70)

    # 构建相同的树
    root_values = [1, 2, 3]
    subRoot_values = [1, 2, 3]

    root = build_tree(root_values)
    subRoot = build_tree(subRoot_values)

    print("主树结构:")
    print_tree(root)
    print("\n子树结构:")
    print_tree(subRoot)
    print("\n搜索过程:")

    solution = Solution()
    result = solution.isSubtree(root, subRoot)

    print(f"\n📋 测试结果: {result} (期望: True)")
    print(f"✅ {'通过' if result == True else '失败'}")
    return result == True


def test_case_4():
    print("\n" + "=" * 70)
    print("测试用例4: 空子树")
    print("=" * 70)

    root_values = [1, 2, 3]
    subRoot_values = []

    root = build_tree(root_values)
    subRoot = build_tree(subRoot_values)

    print("主树结构:")
    print_tree(root)
    print("\n子树结构: 空树")
    print("\n搜索过程:")

    solution = Solution()
    result = solution.isSubtree(root, subRoot)

    print(f"\n📋 测试结果: {result} (期望: True)")
    print(f"✅ {'通过' if result == True else '失败'}")
    return result == True


def test_case_5():
    print("\n" + "=" * 70)
    print("测试用例5: 空主树")
    print("=" * 70)

    root_values = []
    subRoot_values = [1]

    root = build_tree(root_values)
    subRoot = build_tree(subRoot_values)

    print("主树结构: 空树")
    print("\n子树结构:")
    print_tree(subRoot)
    print("\n搜索过程:")

    solution = Solution()
    result = solution.isSubtree(root, subRoot)

    print(f"\n📋 测试结果: {result} (期望: False)")
    print(f"✅ {'通过' if result == False else '失败'}")
    return result == False


def test_case_6():
    print("\n" + "=" * 70)
    print("测试用例6: 子树是叶子节点")
    print("=" * 70)

    # 构建主树: [1,2,3,4,5]
    #      1
    #     / \
    #    2   3
    #   / \
    #  4   5
    root_values = [1, 2, 3, 4, 5]

    # 构建子树: [5]
    subRoot_values = [5]

    root = build_tree(root_values)
    subRoot = build_tree(subRoot_values)

    print("主树结构:")
    print_tree(root)
    print("\n子树结构:")
    print_tree(subRoot)
    print("\n搜索过程:")

    solution = Solution()
    result = solution.isSubtree(root, subRoot)

    print(f"\n📋 测试结果: {result} (期望: True)")
    print(f"✅ {'通过' if result == True else '失败'}")
    return result == True


def test_case_7():
    print("\n" + "=" * 70)
    print("测试用例7: 复杂结构中的子树")
    print("=" * 70)

    # 构建主树: [3,4,5,1,2,6,7,8,9]
    #        3
    #       / \
    #      4   5
    #     / \   \
    #    1   2   6
    #   /       / \
    #  8       9   7
    root_values = [3, 4, 5, 1, 2, None, 6, 8, None, None, None, 9, 7]

    # 构建子树: [4,1,2,8]
    #      4
    #     / \
    #    1   2
    #   /
    #  8
    subRoot_values = [4, 1, 2, 8]

    root = build_tree(root_values)
    subRoot = build_tree(subRoot_values)

    print("主树结构:")
    print_tree(root)
    print("\n子树结构:")
    print_tree(subRoot)
    print("\n搜索过程:")

    solution = Solution()
    result = solution.isSubtree(root, subRoot)

    print(f"\n📋 测试结果: {result} (期望: True)")
    print(f"✅ {'通过' if result == True else '失败'}")
    return result == True


# 运行所有测试
if __name__ == "__main__":
    print("子树判断验证测试")
    print("=" * 70)

    test_cases = [
        test_case_1,  # 经典包含子树
        test_case_2,  # 不包含子树
        test_case_3,  # 子树就是主树
        test_case_4,  # 空子树
        test_case_5,  # 空主树
        test_case_6,  # 子树是叶子节点
        test_case_7  # 复杂结构中的子树
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
    print("\n💡 子树判断算法逻辑:")
    print("1. ✅ 空子树 → 任何树都包含空子树")
    print("2. ❌ 空主树但子树不为空 → 不包含")
    print("3. 🔍 检查当前节点开始的子树是否匹配")
    print("4. 🧭 递归检查左右子树")
    print("5. 📊 只要有一个分支找到就返回True")