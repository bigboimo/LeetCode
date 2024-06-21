# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        s,f = dummy, dummy
        i = 0

        while f and f.next:
            f = f.next

            if i >= n:
                s = s.next

            i += 1
        print(s)
        print(f)

        s.next = s.next.next


        return dummy.next
            