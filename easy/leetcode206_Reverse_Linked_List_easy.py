# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        使用哈希表法深拷贝带随机指针的链表
        """
        if not head:
            return None

        # 创建原节点到新节点的映射
        mapping = {}

        # 第一次遍历：创建所有新节点，建立映射关系
        current = head
        while current:
            mapping[current] = Node(current.val)
            current = current.next

        # 第二次遍历：设置新节点的next和random指针
        current = head
        while current:
            # 设置next指针
            if current.next:
                mapping[current].next = mapping[current.next]
            # 设置random指针
            if current.random:
                mapping[current].random = mapping[current.random]
            current = current.next

        return mapping[head]


# 辅助函数：创建测试链表
def create_linked_list(nodes):
    """
    根据节点列表创建链表
    nodes: [[val, random_index], ...]
    """
    if not nodes:
        return None

    # 先创建所有节点
    node_list = []
    for val, _ in nodes:
        node_list.append(Node(val))

    # 设置next和random指针
    for i, (_, random_index) in enumerate(nodes):
        if i < len(nodes) - 1:
            node_list[i].next = node_list[i + 1]
        if random_index is not None:
            node_list[i].random = node_list[random_index]

    return node_list[0]


# 辅助函数：打印链表（用于调试）
def print_linked_list(head):
    """
    打印链表结构，显示val和random指向的val
    """
    if not head:
        print("空链表")
        return

    # 创建节点到索引的映射
    node_to_index = {}
    current = head
    index = 0
    while current:
        node_to_index[current] = index
        current = current.next
        index += 1

    # 打印每个节点的信息
    current = head
    result = []
    while current:
        random_info = node_to_index.get(current.random, "null")
        result.append(f"[{current.val}, random->{random_info}]")
        current = current.next

    print(" → ".join(result))


# 测试示例
if __name__ == "__main__":
    solution = Solution()

    # 测试用例1：LeetCode官方示例
    print("测试用例1:")
    # [[7,null],[13,0],[11,4],[10,2],[1,0]]
    head1 = create_linked_list([
        [7, None],  # 索引0，random为null
        [13, 0],  # 索引1，random指向索引0(7)
        [11, 4],  # 索引2，random指向索引4(1)
        [10, 2],  # 索引3，random指向索引2(11)
        [1, 0]  # 索引4，random指向索引0(7)
    ])

    print("原链表:")
    print_linked_list(head1)

    copied_head1 = solution.copyRandomList(head1)
    print("拷贝后:")
    print_linked_list(copied_head1)
    print("是否是深拷贝:", head1 != copied_head1)  # 应该为True
    print()

    # 测试用例2：单个节点
    print("测试用例2:")
    head2 = create_linked_list([[1, None]])
    print("原链表:")
    print_linked_list(head2)

    copied_head2 = solution.copyRandomList(head2)
    print("拷贝后:")
    print_linked_list(copied_head2)
    print("是否是深拷贝:", head2 != copied_head2)
    print()

    # 测试用例3：空链表
    print("测试用例3:")
    head3 = None
    copied_head3 = solution.copyRandomList(head3)
    print("空链表拷贝:", copied_head3)