# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):
        """
        使用快慢指针找到链表的中间节点
        """
        if not head:
            return None

        slow = head  # 慢指针，每次移动1步
        fast = head  # 快指针，每次移动2步

        # 当fast到达末尾时，slow就在中间
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


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
        [1, 2, 3, 4, 5],  # 奇数长度，中间节点3
        [1, 2, 3, 4, 5, 6],  # 偶数长度，中间节点4（第二个）
        [1, 2],  # 两个节点，中间节点2
        [1],  # 单节点，中间节点1
        [],  # 空链表
        [1, 2, 3, 4],  # 偶数长度，中间节点3
    ]

    for i, arr in enumerate(test_cases):
        head = create_linked_list(arr)
        print(f"测试用例 {i + 1}:")
        print(f"原始链表: ", end="")
        print_linked_list(head)

        result = solution.middleNode(head)
        if result:
            print(f"中间节点: {result.val}")
        else:
            print(f"中间节点: 空链表")
        print()