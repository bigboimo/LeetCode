# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = dummy = ListNode()
        print(res)

        while list1 and list2:
            if list1.val > list2.val:
                res.next = list2
                res = list2
                list2 = list2.next
            elif list1.val < list2.val:
                res.next = list1
                res = list1
                list1 = list1.next
            else:
                res.next = list2
                res = list2
                list2 = list2.next

         

        if list1:
            res.next = list1
          
        if list2:
            res.next = list2
           

        print(dummy)

        return dummy.next

        