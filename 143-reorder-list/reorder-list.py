# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head 

        #Find the middle point (slow) O(n)
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        prev, curr = None, slow
        #Reverse the second half of the linked list o(n/2)
        while curr:
            temp = curr.next 
            curr.next = prev
            prev = curr 
            curr = temp


        start, mid = head, slow
        
        res = head
        #Connect the first half to the second reversed half
        while prev and prev.next:
            temp1 = head.next
            temp2 = prev.next

            head.next = prev
            head = temp1

            prev.next = head
            prev = temp2
        

                        