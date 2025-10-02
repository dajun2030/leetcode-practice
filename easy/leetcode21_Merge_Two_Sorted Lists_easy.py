# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        """
        迭代法合并两个有序链表
        """
        # 创建虚拟头节点
        dummy = ListNode(0)
        current = dummy

        # 同时遍历两个链表
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # 连接剩余部分
        current.next = list1 if list1 else list2

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
        ([1, 3, 5], [2, 4, 6]),  # 标准示例
        ([1, 2, 4], [1, 3, 4]),  # 有重复元素
        ([], [1, 2, 3]),  # list1为空
        ([1, 2, 3], []),  # list2为空
        ([], []),  # 两个都为空
        ([5], [1, 2, 4]),  # 长度不同
    ]

    for i, (arr1, arr2) in enumerate(test_cases):
        list1 = create_linked_list(arr1)
        list2 = create_linked_list(arr2)

        print(f"测试用例 {i + 1}:")
        print(f"list1: ", end="")
        print_linked_list(list1)
        print(f"list2: ", end="")
        print_linked_list(list2)

        result = solution.mergeTwoLists(list1, list2)
        print(f"合并后: ", end="")
        print_linked_list(result)
        print()