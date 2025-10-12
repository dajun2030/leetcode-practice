import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 创建虚拟头节点
        dummy = ListNode(0)
        current = dummy

        # 最小堆，存储 (节点值, 节点)
        min_heap = []

        # 将所有链表的头节点加入堆中
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(min_heap, (head.val, i, head))

        # 不断从堆中取出最小节点
        while min_heap:
            val, idx, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next

            # 如果该链表还有下一个节点，加入堆中
            if node.next:
                heapq.heappush(min_heap, (node.next.val, idx, node.next))

        return dummy.next


def create_linked_list(arr):
    """从数组创建链表"""
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def linked_list_to_list(head):
    """链表转数组"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def test_mergeKLists():
    solution = Solution()

    # 测试用例
    test_cases = [
        # 用例1: 三个有序链表
        [
            create_linked_list([1, 4, 5]),
            create_linked_list([1, 3, 4]),
            create_linked_list([2, 6])
        ],
        # 用例2: 空链表
        [],
        # 用例3: 包含空链表
        [
            create_linked_list([1, 2, 3]),
            None,
            create_linked_list([4, 5, 6])
        ],
        # 用例4: 单个链表
        [
            create_linked_list([1, 2, 3])
        ]
    ]

    expected_results = [
        [1, 1, 2, 3, 4, 4, 5, 6],
        [],
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3]
    ]

    print("🧪 Merge k Sorted Lists 测试")
    print("=" * 50)

    for i, (lists, expected) in enumerate(zip(test_cases, expected_results), 1):
        result_head = solution.mergeKLists(lists)
        result_list = linked_list_to_list(result_head)

        status = "✅" if result_list == expected else "❌"
        print(f"测试 {i}: {status}")
        print(f"  结果: {result_list}")
        print(f"  期望: {expected}")
        print()


# 运行测试
test_mergeKLists()