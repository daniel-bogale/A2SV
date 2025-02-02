
class Solution:
    def removeNthFromEnd(self, head,n):
        l=dummy=ListNode(0,head)
        r=head
        while n>0:
            r=r.next
            n-=1
        while r:
            l=l.next
            r=r.next
        l.next=l.next.next
        return dummy.next

        
