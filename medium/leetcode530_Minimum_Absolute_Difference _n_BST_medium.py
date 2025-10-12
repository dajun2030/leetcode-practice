class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 第1行：初始化栈、当前指针、前一个节点值、最小差值
        stack = []
        curr = root
        prev = None
        min_diff = float('inf')

        print(f"🚀 开始寻找最小绝对差")
        print(f"初始: stack={[]}, curr={root.val}, prev={prev}, min_diff={min_diff}")

        # 第2行：开始主循环

            print(f"\n=== 主循环开始 ===")
            print(f"    stack={[n.val for n in stack]}, curr={curr.val if curr else None}")

            # 第3行：向左遍历到最左节点
            while curr:
                print(f"  ↙️ 向左遍历: curr={curr.val}")
                stack.append(curr)
                print(f"    入栈: {curr.val} → stack={[n.val for n in stack]}")
                curr = curr.left
                print(f"    移动到左子节点: curr={curr.val if curr else None}")

            # 第4行：弹出栈顶节点
            curr = stack.pop()
            print(f"  🎯 弹出节点: {curr.val}")
            print(f"    弹出后 stack={[n.val for n in stack]}")

            # 第5行：计算与前一节点的差值
            if prev is not None:
                diff = curr.val - prev
                print(f"  📊 计算差值: {curr.val} - {prev} = {diff}")
                min_diff = min(min_diff, diff)
                print(f"    更新最小差值: min({min_diff}, {diff}) = {min_diff}")
            else:
                print(f"  📊 第一个节点 {curr.val}，跳过差值计算")

            # 第6行：更新前一节点值
            prev = curr.val
            print(f"  🔄 更新prev: {prev}")

            # 第7行：转向右子树
            curr = curr.right
            print(f"  ↘️ 转向右子树: curr={curr.val if curr else None}")

        # 第8行：返回结果
        print(f"\n🎉 最终最小绝对差: {min_diff}")
        return min_diff


# 构建测试树: [4,2,6,1,3]
#     4
#    / \
#   2   6
#  / \
# 1   3
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

print("测试树结构:")
print("    4")
print("   / \\")
print("  2   6")
print(" / \\")
print("1   3")
print("\n中序遍历顺序: 1 → 2 → 3 → 4 → 6")
print("期望最小绝对差: 1")
print("\n" + "=" * 50)

solution = Solution()
result = solution.getMinimumDifference(root)
print(f"\n✅ 测试结果: {result} (期望: 1)")