
def maxDepth(root):
    if not root:
        return 0

    left_depth=maxDepth(root.left)
    right_depth=maxDepth(root.right)
    return max(left_depth, right_depth) + 1

from binarytree import build

# 一行代码构建树
values = [3, 9, 20, None, None, 15, 7]
tree = build(values)
print(tree)  # 自动可视化打印

# 直接使用
depth = maxDepth(tree)
print(depth)