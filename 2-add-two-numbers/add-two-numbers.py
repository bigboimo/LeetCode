# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        curr1 = l1
        curr2 = l2

        group1 = []
        group2 = []

        num1 = ""
        num2 = ""


        while curr1:
            group1.append(curr1.val)
            curr1 = curr1.next

        while curr2:
            group2.append(curr2.val)
            curr2 = curr2.next


        for s in reversed(group1):
            num1 += str(s)

        for s in reversed(group2):
            num2 += str(s)

        print(num1, num2)

        res = int(num1) + int(num2)

        res = str(res)

        ptr = nodes = ListNode()

        for s in reversed(res):
            print(s)
            node = ListNode((int(s)))
            nodes.next = node
            nodes = node

        print(ptr)

        return ptr.next