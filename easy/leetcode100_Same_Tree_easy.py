# def isSameTree(self, p, q):
#     if not p and not q:
#         return True
#
#     if not p or not q:
#         return False
#
#     if p.val!=q.val:
#         return False
#
#     return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)

#######################################################################

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # 第1行：两个节点都为空
        if not p and not q:
            print(f"    ✅ 两个节点都为空 → 返回 True")
            return True

        # 第2行：一个节点为空，另一个不为空
        if not p or not q:
            print(f"    ❌ 一个为空一个不为空: p={p.val if p else 'None'}, q={q.val if q else 'None'} → 返回 False")
            return False

        # 第3行：节点值不相等
        if p.val != q.val:
            print(f"    ❌ 节点值不相等: p.val={p.val}, q.val={q.val} → 返回 False")
            return False

        print(f"    🔍 节点 p={p.val}, q={q.val} 相同，继续检查子树...")

        # 第4行：递归检查左右子树
        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)

        result = left_same and right_same
        print(
            f"    📊 节点 {p.val}: 左子树{'相同' if left_same else '不同'}, 右子树{'相同' if right_same else '不同'} → {result}")

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
    print("测试用例1: 相同的树 [1,2,3]")
    print("=" * 70)

    # 构建两棵相同的树
    #     1         1
    #    / \       / \
    #   2   3     2   3
    p_values = [1, 2, 3]
    q_values = [1, 2, 3]

    p = build_tree(p_values)
    q = build_tree(q_values)

    print("树 p:")
    print_tree(p)
    print("\n树 q:")
    print_tree(q)
    print("\n比较过程:")

    solution = Solution()
    result = solution.isSameTree(p, q)

    print(f"\n📋 测试结果: {result} (期望: True)")
    print(f"✅ {'通过' if result == True else '失败'}")
    return result == True


def test_case_2():
    print("\n" + "=" * 70)
    print("测试用例2: 结构不同的树")
    print("=" * 70)

    # 构建结构不同的树
    #     1         1
    #    /           \
    #   2             2
    p_values = [1, 2]
    q_values = [1, None, 2]

    p = build_tree(p_values)
    q = build_tree(q_values)

    print("树 p:")
    print_tree(p)
    print("\n树 q:")
    print_tree(q)
    print("\n比较过程:")

    solution = Solution()
    result = solution.isSameTree(p, q)

    print(f"\n📋 测试结果: {result} (期望: False)")
    print(f"✅ {'通过' if result == False else '失败'}")
    return result == False


def test_case_3():
    print("\n" + "=" * 70)
    print("测试用例3: 值不同的树")
    print("=" * 70)

    # 构建值不同的树
    #     1         1
    #    / \       / \
    #   2   1     1   2
    p_values = [1, 2, 1]
    q_values = [1, 1, 2]

    p = build_tree(p_values)
    q = build_tree(q_values)

    print("树 p:")
    print_tree(p)
    print("\n树 q:")
    print_tree(q)
    print("\n比较过程:")

    solution = Solution()
    result = solution.isSameTree(p, q)

    print(f"\n📋 测试结果: {result} (期望: False)")
    print(f"✅ {'通过' if result == False else '失败'}")
    return result == False


def test_case_4():
    print("\n" + "=" * 70)
    print("测试用例4: 空树")
    print("=" * 70)

    p = None
    q = None

    print("树 p: 空树")
    print("树 q: 空树")
    print("\n比较过程:")

    solution = Solution()
    result = solution.isSameTree(p, q)

    print(f"\n📋 测试结果: {result} (期望: True)")
    print(f"✅ {'通过' if result == True else '失败'}")
    return result == True


def test_case_5():
    print("\n" + "=" * 70)
    print("测试用例5: 一个空树一个非空树")
    print("=" * 70)

    p = None
    q_values = [1, 2, 3]
    q = build_tree(q_values)

    print("树 p: 空树")
    print("\n树 q:")
    print_tree(q)
    print("\n比较过程:")

    solution = Solution()
    result = solution.isSameTree(p, q)

    print(f"\n📋 测试结果: {result} (期望: False)")
    print(f"✅ {'通过' if result == False else '失败'}")
    return result == False


def test_case_6():
    print("\n" + "=" * 70)
    print("测试用例6: 复杂相同的树")
    print("=" * 70)

    # 构建复杂的相同树
    #        1              1
    #       / \            / \
    #      2   3          2   3
    #     / \            / \
    #    4   5          4   5
    p_values = [1, 2, 3, 4, 5]
    q_values = [1, 2, 3, 4, 5]

    p = build_tree(p_values)
    q = build_tree(q_values)

    print("树 p:")
    print_tree(p)
    print("\n树 q:")
    print_tree(q)
    print("\n比较过程:")

    solution = Solution()
    result = solution.isSameTree(p, q)

    print(f"\n📋 测试结果: {result} (期望: True)")
    print(f"✅ {'通过' if result == True else '失败'}")
    return result == True


def test_case_7():
    print("\n" + "=" * 70)
    print("测试用例7: 复杂不同的树")
    print("=" * 70)

    # 构建复杂的不同树（一个子树不同）
    #        1              1
    #       / \            / \
    #      2   3          2   3
    #     / \            / \
    #    4   5          4   6
    p_values = [1, 2, 3, 4, 5]
    q_values = [1, 2, 3, 4, 6]

    p = build_tree(p_values)
    q = build_tree(q_values)

    print("树 p:")
    print_tree(p)
    print("\n树 q:")
    print_tree(q)
    print("\n比较过程:")

    solution = Solution()
    result = solution.isSameTree(p, q)

    print(f"\n📋 测试结果: {result} (期望: False)")
    print(f"✅ {'通过' if result == False else '失败'}")
    return result == False


# 运行所有测试
if __name__ == "__main__":
    print("相同的树验证测试")
    print("=" * 70)

    test_cases = [
        test_case_1,  # 相同的简单树
        test_case_2,  # 结构不同
        test_case_3,  # 值不同
        test_case_4,  # 都为空
        test_case_5,  # 一个空一个非空
        test_case_6,  # 复杂相同树
        test_case_7  # 复杂不同树
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
    print("\n💡 算法逻辑总结:")
    print("1. ✅ 两个节点都为空 → 相同")
    print("2. ❌ 一个为空一个不为空 → 不同")
    print("3. ❌ 节点值不相等 → 不同")
    print("4. 🔍 递归检查: 左子树相同 AND 右子树相同 → 相同")

    #########################################################################
    #BFS
    from collections import deque
    class Solution:
        def isSameTree(self,p,q):
            queue=deque([p,q])
            while queue:
                node_p,node_q=queue.popleft()
                if not node_p and not node_q:
                    continue

                if not node_p or not node_q or node_p.val !=node_q.val:
                    return False
                queue.append([node_p.left,node_q.left])
                queue.append([node_p.right,node_q.right])

            return True
