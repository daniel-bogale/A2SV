# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next

        current = head
        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return head
