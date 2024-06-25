# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        res = dummy = ListNode()

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            #arithmetic
            total = v1 + v2 + carry
            carry = total // 10
            total = total % 10

            dummy.next = ListNode(total)
            
            #Iteration over all 
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            dummy = dummy.next

        return res.next



