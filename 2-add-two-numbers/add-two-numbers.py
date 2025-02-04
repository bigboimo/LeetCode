# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        curr1, curr2 = l1, l2

        res = 0
        idx = 1
        while curr1:
            curr1.val *= idx
            idx *= 10
            res += curr1.val
            curr1 = curr1.next
        
        idx = 1
        while curr2:
            curr2.val *= idx
            idx *= 10
            res += curr2.val
            curr2 = curr2.next
        
        res = str(res)
        
        finalList = ListNode()
        ptr = finalList
        for i in range(len(res) - 1, -1, -1):
            finalList.next = ListNode(int(res[i]))
            finalList = finalList.next
        
        print(ptr)
        return ptr.next
            



        


