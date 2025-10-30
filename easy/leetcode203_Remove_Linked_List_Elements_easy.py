class listNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

def createdListNode(arr):
    if arr is None:
        return None
    head=listNode(arr[0])
    current=head

    for val in arr[1:]:
        current.next=listNode(val)
        current=current.next
    return head

def removeElements(head, val):
    dummy=listNode(0,head)
    current=dummy

    while current.next:
        if current.next.val==val:
            current.next=current.next.next
        else:
            current=current.next
    printList(dummy.next)
    return dummy.next

def printList(head):
    current=head
    while current:
        print(f'{current.val}->',end='')
        current=current.next
    print('None')

if __name__=='__main__':
    arr=[1,2,3,4,6,7,5,6,8,9,6,4]
    head=createdListNode(arr)
    removeElements(head,6)


