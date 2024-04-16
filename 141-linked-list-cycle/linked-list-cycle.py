# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        intersectionFound = False

        #Loop to determine intersection of slow and fast pointers, if no cycle the loop ends as a null node is eventually visited. O(n) time complexity
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                intersectionFound = True
                break

        return intersectionFound


            

        