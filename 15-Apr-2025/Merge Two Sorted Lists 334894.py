# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/description/

class Solution(object):
    def mergeTwoLists(self,list1,list2):
        if list1==None:
            return list2
        if list2==None:
            return list1 
        if list1.val<=list2.val:
            temp=head=ListNode(list1.val)
            list1=list1.next 
        else:
            temp=head=ListNode(list2.val)
            list2=list2.next 
        while list1 and list2:
            if list1.val<=list2.val:
                temp.next=ListNode(list1.val)
                list1=list1.next 
            else:
                temp.next=ListNode(list2.val)
                list2=list2.next 
            temp=temp.next 
        temp.next=list1 or list2 
        return  head