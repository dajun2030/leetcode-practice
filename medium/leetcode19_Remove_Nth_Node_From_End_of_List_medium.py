# def removeNthFromEnd(head, n):
#     dummy=ListNode(0)
#     dummy.next=head
#     fast=slow=head
#
#     for _ in range(n):
#         fast=fast.next
#
#     while fast.next:
#         slow=slow.next
#         fast=fast.next
#
#     slow=slow.next.next
#     return dummy.next


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        删除链表的倒数第 n 个节点
        """
        # 创建虚拟头节点，简化边界情况处理
        dummy = ListNode(0)
        dummy.next = head

        fast = dummy  # 快指针
        slow = dummy  # 慢指针

        # 快指针先前进 n 步
        for _ in range(n):
            fast = fast.next

        # 两个指针同时前进，直到快指针到达末尾
        while fast.next:
            slow = slow.next
            fast = fast.next

        # 删除倒数第 n 个节点
        slow.next = slow.next.next

        return dummy.next


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
        ([1, 2, 3, 4, 5], 2),  # 删除倒数第2个节点(4)
        ([1], 1),  # 删除唯一节点
        ([1, 2], 1),  # 删除尾节点
        ([1, 2], 2),  # 删除头节点
        ([1, 2, 3], 3),  # 删除头节点(n=长度)
        ([1, 2, 3, 4, 5], 5),  # 删除头节点(n=长度)
    ]

    for i, (arr, n) in enumerate(test_cases):
        head = create_linked_list(arr)
        print(f"测试用例 {i + 1}:")
        print(f"原始链表: ", end="")
        print_linked_list(head)
        print(f"n = {n}")

        result = solution.removeNthFromEnd(head, n)
        print(f"删除后:   ", end="")
        print_linked_list(result)
        print()