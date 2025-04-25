# Problem: Middle of the Linked List - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middleNode = head
        tailNode = head
        while tailNode.next and tailNode.next.next:
            middleNode = middleNode.next
            tailNode = tailNode.next.next
        
        if tailNode.next:
            return middleNode.next
        
        return middleNode
        