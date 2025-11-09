# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        for l_list in lists:
            current = l_list
            while current:  
                heapq.heappush(heap, current.val)
                current = current.next
        
        dummy = ListNode(0)
        current = dummy
        while heap:
            val = heapq.heappop(heap)
            current.next = ListNode(val)
            current = current.next
        
        return dummy.next   