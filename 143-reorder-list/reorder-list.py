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

        slow, fast = head, head.next
        #Find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        #Disconnect first from second
        slow.next = None

        #Reverse second part of the linked list
        prev, curr = None, second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        second = prev
        first = head
        
        #Merging the two lists
        while second:
            temp1 = first.next
            first.next = second
            first = temp1

            temp2 = second.next
            second.next = first
            second = temp2

        