# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head) -> bool:
        """
        使用快慢指针检测链表是否有环
        """
        if not head or not head.next:
            return False

        slow = head  # 慢指针，每次移动1步
        fast = head  # 快指针，每次移动2步

        while fast and fast.next:
            slow = slow.next  # 慢指针移动1步
            fast = fast.next.next  # 快指针移动2步

            if slow == fast:  # 如果相遇，说明有环
                return True

        return False  # 快指针到达末尾，说明无环


# 辅助函数：创建有环链表
def create_linked_list_with_cycle(arr, pos):
    """
    创建链表，并在指定位置形成环
    arr: 节点值列表
    pos: 环的连接位置（尾节点连接到该位置的节点）
    """
    if not arr:
        return None

    # 创建所有节点
    nodes = []
    for val in arr:
        nodes.append(ListNode(val))

    # 连接节点
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # 形成环（如果pos有效）
    if 0 <= pos < len(nodes):
        nodes[-1].next = nodes[pos]

    return nodes[0]


# 辅助函数：创建无环链表
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# 测试示例
if __name__ == "__main__":
    solution = Solution()

    # 测试用例1：有环链表
    print("测试用例1：有环链表")
    head1 = create_linked_list_with_cycle([3, 2, 0, -4], 1)
    result1 = solution.hasCycle(head1)
    print(f"结果: {result1}")  # 应该输出 True

    # 测试用例2：无环链表
    print("\n测试用例2：无环链表")
    head2 = create_linked_list([1, 2, 3, 4])
    result2 = solution.hasCycle(head2)
    print(f"结果: {result2}")  # 应该输出 False

    # 测试用例3：单个节点无环
    print("\n测试用例3：单个节点无环")
    head3 = create_linked_list([1])
    result3 = solution.hasCycle(head3)
    print(f"结果: {result3}")  # 应该输出 False

    # 测试用例4：单个节点自成环
    print("\n测试用例4：单个节点自成环")
    head4 = create_linked_list_with_cycle([1], 0)
    result4 = solution.hasCycle(head4)
    print(f"结果: {result4}")  # 应该输出 True

    # 测试用例5：空链表
    print("\n测试用例5：空链表")
    result5 = solution.hasCycle(None)
    print(f"结果: {result5}")  # 应该输出 False

    # 测试用例6：两个节点形成环
    print("\n测试用例6：两个节点形成环")
    head6 = create_linked_list_with_cycle([1, 2], 0)
    result6 = solution.hasCycle(head6)
    print(f"结果: {result6}")  # 应该输出 True