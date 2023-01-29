
class Solution(object):
    def deleteDuplicates(self, head):
        dummy=ListNode(0,head)
        slow=dummy
        while head:
            if head.next and head.val==head.next.val:
                while head.next and head.val==head.next.val:
                    head=head.next
                slow.next=head.next
            else:
                slow=slow.next
            head=head.next
        return dummy.next
