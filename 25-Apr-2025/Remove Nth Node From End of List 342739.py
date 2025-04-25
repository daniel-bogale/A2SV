# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        current = head
        while current:
            current = current.next
            length += 1

        if n == length:
            return head.next

        index = length - n - 1
        current = head
        for i in range(index):
            current = current.next

        current.next = current.next.next
        return head
