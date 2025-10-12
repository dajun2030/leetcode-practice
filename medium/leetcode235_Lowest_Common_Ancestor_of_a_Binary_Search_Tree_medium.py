# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         current = root
#
#         while current:
#             # 如果p和q都在左子树
#             if p.val < current.val and q.val < current.val:
#                 current = current.left
#             # 如果p和q都在右子树
#             elif p.val > current.val and q.val > current.val:
#                 current = current.right
#             # 否则当前节点就是LCA
#             else:
#                 return current

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current = root

        while current:
            print(f"当前节点: {current.val}, p={p.val}, q={q.val}")

            # 如果p和q都在左子树
            if p.val < current.val and q.val < current.val:
                print(f"  → p和q都在左子树，移动到左孩子")
                current = current.left
            # 如果p和q都在右子树
            elif p.val > current.val and q.val > current.val:
                print(f"  → p和q都在右子树，移动到右孩子")
                current = current.right
            # 否则当前节点就是LCA
            else:
                print(f"  → p和q在不同侧，LCA是: {current.val}")
                return current


def build_test_tree():
    """构建测试用的BST"""
    # 创建所有节点
    nodes = {}
    for val in [6, 2, 8, 0, 4, 7, 9, 3, 5]:
        nodes[val] = TreeNode(val)

    # 构建树结构
    nodes[6].left = nodes[2]
    nodes[6].right = nodes[8]

    nodes[2].left = nodes[0]
    nodes[2].right = nodes[4]

    nodes[8].left = nodes[7]
    nodes[8].right = nodes[9]

    nodes[4].left = nodes[3]
    nodes[4].right = nodes[5]

    return nodes


def test_lowestCommonAncestor():
    solution = Solution()
    nodes = build_test_tree()

    test_cases = [
        (2, 8, 6, "p和q在根节点两侧"),
        (2, 4, 2, "一个节点是另一个的祖先"),
        (3, 5, 4, "都在左子树的右侧"),
        (7, 9, 8, "都在右子树的右侧"),
        (0, 5, 2, "跨越多个层级"),
        (6, 8, 6, "根节点是其中一个节点")
    ]

    print("=" * 50)
    print("BST结构:")
    print("        6")
    print("       / \\")
    print("      2   8")
    print("     / \\ / \\")
    print("    0  4 7  9")
    print("      / \\")
    print("     3   5")
    print("=" * 50)

    for p_val, q_val, expected, description in test_cases:
        print(f"\n测试: {description}")
        print(f"p={p_val}, q={q_val}")

        result = solution.lowestCommonAncestor(nodes[6], nodes[p_val], nodes[q_val])

        print(f"预期LCA: {expected}, 实际LCA: {result.val}")
        print(f"结果: {'✅ 通过' if result.val == expected else '❌ 失败'}")
        print("-" * 30)


if __name__ == "__main__":
    test_lowestCommonAncestor()