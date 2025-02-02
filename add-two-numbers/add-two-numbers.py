class Solution:
    def addTwoNumbers(self, l1, l2):
        
        carry=0
        
        head=ListNode()
        
        curr=head
        while l1 or l2 or carry:
            
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0
            
            value=v1+v2+carry

            if value>9:
                value=value%10
                carry=1
            else:
                carry=0
            
            curr.next=ListNode(value)
            
            
            curr=curr.next
            
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None

     
        return head.next
            
