# 定义节点（LeetCode 已内置，本地调试需复制）
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # 1. 空链表直接返回
        if not head:
            return None

        # 2. 字典：原节点 -> 新节点（哈希映射）
        d: dict[Node, Node] = {}
        curr = head

        # 3. 一次遍历：创建新节点并同时连好 next 与 random
        while curr:
            # 3-1 当前节点尚未复制，就新建一个同值节点
            if curr not in d:
                d[curr] = Node(curr.val, None, None)

            # 3-2 处理 next 指针
            if curr.next:
                if curr.next not in d:                      # next 节点还没复制
                    d[curr.next] = Node(curr.next.val, None, None)
                d[curr].next = d[curr.next]                 # 把新节点的 next 连上去

            # 3-3 处理 random 指针
            if curr.random:
                if curr.random not in d:                    # random 节点还没复制
                    d[curr.random] = Node(curr.random.val, None, None)
                d[curr].random = d[curr.random]             # 把新节点的 random 连上去

            # 3-4 指针后移，继续处理下一个旧节点
            curr = curr.next

        # 4. 返回新链表的头节点
        return d[head]

if __name__ == '__main__':
    # 构造 1->2->3，random 分别指向 3, 1, None
    n3 = Node(3); n2 = Node(2); n1 = Node(1)
    n1.next, n2.next = n2, n3
    n1.random, n2.random, n3.random = n3, n1, None

    new_head = Solution().copyRandomList(n1)
    cur = new_head
    while cur:
        r = cur.random.val if cur.random else "None"
        print(f"node {cur.val}, random -> {r}")
        cur = cur.next