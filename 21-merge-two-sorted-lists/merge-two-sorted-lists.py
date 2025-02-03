# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr1 = list1
        curr2 = list2
        merged = ListNode(0)
        res = merged

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                res.next = curr1
                curr1 = curr1.next
            else: 
                res.next = curr2
                curr2 = curr2.next
            res = res.next

        if curr1:
            res.next = curr1
        
        if curr2:
            res.next = curr2

        return merged.next

        