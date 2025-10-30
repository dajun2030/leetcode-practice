def isPalindrome(head):
    if not head or not head.next:
        return True

    values=[]
    cur=head
    while cur:
        values.append(cur.val)
        cur=cur.next

    left,right=0,len(values)-1
    while left<right:
        if values[left]!=values[right]:
            return False
        else:
            right-=1
            left+=1
    return True

########################################

class Solution:
    def isPalindrome(self,head):
        if not head or not head.next:
            return True

        slow,fast=head,head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next

        second_half_start=self.reverse_list(slow.next)

        first,second=head,second_half_start
        result=True
        while second:
            if first.val!=second.val:
                return False
                break
            first=first.next
            second=second.next

        slow.next=self.reverse_list(second_half_start)

        return result

    def reverse_list(self,head):
        prev=None
        cur=head
        while cur:
            next_temp=cur.next
            cur.next=prev
            prev=cur
            cur=next_temp
        return prev

