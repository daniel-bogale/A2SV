class Solution(object):
    def middleNode(self, head):
        
        fast=slow=head
        while fast:
            if fast.next:
                fast=fast.next.next
                slow=slow.next
            else:
                break

        return slow
