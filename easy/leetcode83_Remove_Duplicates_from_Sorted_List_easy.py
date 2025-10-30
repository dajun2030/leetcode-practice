from typing import Optional  # 添加导入


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head


def create_linked_list(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_linked_list(head):
    result = []
    current = head
    while current:
        result.append(str(current.val))
        current = current.next
    # 修正：在循环结束后打印
    if result:
        print("->".join(result))
    else:
        print("空链表")


if __name__ == "__main__":
    solution = Solution()  # 创建Solution实例

    test_cases = [
        [1, 1, 2],  # 基础示例
        [1, 1, 2, 3, 3],  # 多个重复
        [1, 2, 3, 4, 5],  # 无重复
        [1, 1, 1],  # 全部重复
        [1],  # 单节点
        [],  # 空链表
    ]

    for i, arr in enumerate(test_cases):
        head = create_linked_list(arr)
        print(f"测试用例 {i + 1}:")
        print(f"输入: ", end="")
        print_linked_list(head)

        # 修正：通过Solution实例调用方法
        result = solution.deleteDuplicates(head)
        print(f"输出: ", end="")
        print_linked_list(result)
        print()

################################################
#递归法
def deleteDuplicates_recursive(head):
    if not head or not head.next:
        return head

    head.next=deleteDuplicates_recursive(head.next)

    if head.val==head.next.val:
        return head.next
    else:
        return head



