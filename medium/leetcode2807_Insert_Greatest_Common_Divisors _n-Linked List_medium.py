# def insertGreatestCommonDivisors(head):
#     current=head
#
#     while current and current.next:
#         common_divisor=ListNode(gcd(current.val,current.next.val))
#
#         common_divisor.next=current.next
#         current.next=common_divisor
#
#         current=common_divisor.next
#
#     return head

###############################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# class Solution:
#     def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next:
#             return head
#
#         current=head
#
#         while current and current.next:
#             gcd_value=self.gcd(current.val,current.next.val)
#
#             new_node=ListNode(gcd_value)
#             new_node.next=current.next
#             current.next=new_node
#
#             current=new_node.next
#         return head
#
#     def gcd(self, a, b):
#         while b:
#             a,b =b,a%b
#         return a
##############################################################

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head):
        """
        在每两个相邻节点之间插入GCD节点
        """
        # 边界情况：空链表或只有一个节点
        if not head or not head.next:
            return head

        current = head

        while current and current.next:
            # 计算当前节点和下一个节点的GCD
            gcd_value = self.gcd(current.val, current.next.val)

            # 创建新节点
            new_node = ListNode(gcd_value)

            # 插入新节点
            new_node.next = current.next
            current.next = new_node

            # 移动到下一个原始节点（跳过新插入的节点）
            current = new_node.next

        return head

    def gcd(self, a, b):
        """
        计算两个数的最大公约数（欧几里得算法）
        """
        while b:
            a, b = b, a % b
        return a


# 辅助函数：创建链表
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# 辅助函数：打印链表
def print_linked_list(head):
    result = []
    current = head
    while current:
        result.append(str(current.val))
        current = current.next
    print(" → ".join(result) if result else "空链表")


# 测试示例
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [18, 6, 10, 3],  # 示例：18→6→10→3 → 18→6→6→2→10→1→3
        [7],  # 单节点
        [],  # 空链表
        [2, 4, 6, 8],  # 连续偶数
        [5, 7],  # 两个质数
        [12, 18, 24],  # 有公约数的序列
    ]

    for i, arr in enumerate(test_cases):
        head = create_linked_list(arr)
        print(f"测试用例 {i + 1}:")
        print(f"原始链表: ", end="")
        print_linked_list(head)

        result = solution.insertGreatestCommonDivisors(head)
        print(f"插入后:   ", end="")
        print_linked_list(result)
        print()


