class Solution:
    def removeNthFromEnd(self, head, n):
        currentElem = head
        nextEl = currentElem.next
        size = 1
        if not nextEl:
            size = 0
            head = head.next
            return head
        
        while nextEl:
            currentElem = nextEl
            nextEl = currentElem.next
            size += 1

        currentElem = head
        nextEl = currentElem.next

        if n == size:
            head = head.next
            return head
        for i in range(size-n-1):
            currentElem = nextEl
            nextEl = currentElem.next
        
        currentElem.next = nextEl.next
        return head


        
