#迭代法
def reverseList(head):
    prev=None
    current=head

    while current:
        next_temp=current.next
        current.next=prev
        prev=current
        current= next_temp

    return prev

#虚拟头节点
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

def reverseList(head):
    dummy=ListNode(0)
    current=head

    while current:
        next_temp=current.next
        current.next=dummy.next
        dummy.next=current
        current=next_temp

    return dummy.next

#递归法
def reverseList(head):
    if not head or not head.next:
        return head

    new_head=reverseList(head.next)
    head.next.next=head
    head.next=None
    return new_head

