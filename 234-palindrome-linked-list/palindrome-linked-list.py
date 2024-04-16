# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        arr = []

        while curr:
            arr.append(curr.val)
            curr = curr.next

        l, r = 0, len(arr) - 1

        while l <= r:

            if arr[l] != arr[r]:
                return False
            
            l += 1
            r -= 1
        
        return True
