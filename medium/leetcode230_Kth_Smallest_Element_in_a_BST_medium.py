# class TreeNode:
#     def __init__(self,val=0,left=None,right=None):
#         self.val=val
#         self.left=left
#         self.right=right
#
#     def kthSmallest(self,root,k):
#         stack=[]
#         curr=root
#         count=0
#
#         while stack and curr:
#             while curr:
#                 stack.append(curr)
#                 curr=curr.left
#
#             curr=stack.pop()
#             count+=1
#
#             if count==k:
#                 return curr.val
#             curr=curr.right
#         return -1

##############################################################
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def kthSmallest(self, root, k):
        stack = []
        curr = root
        count = 0

        print(f"🔍 寻找第{k}小的元素")

        while stack or curr:  # ✅ 正确的条件
            # 向左走到尽头
            while curr:
                stack.append(curr)
                print(f"  向左: {curr.val}入栈")
                curr = curr.left

            # 弹出当前最小节点
            curr = stack.pop()
            count += 1
            print(f"🎯 弹出: {curr.val}, count={count}")

            # 检查是否找到
            if count == k:
                print(f"🎉 找到第{k}小的元素: {curr.val}")
                return curr.val

            # 转向右子树
            print(f"  转向右子树")
            curr = curr.right

        return -1


# 测试
def test():
    # 构建树: [3,1,4,null,2]
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)

    print("树结构:")
    print("    3")
    print("   / \\")
    print("  1   4")
    print("   \\")
    print("    2")
    print("\n中序遍历: 1 → 2 → 3 → 4")
    print()

    solution = Solution()
    result = solution.kthSmallest(root, 3)
    print(f"\n最终结果: {result} (期望: 3)")


test()