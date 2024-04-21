# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lastA, lastB = headA, headB
        lenA, lenB = 0, 0


        while lastA and lastA.next:
            lastA = lastA.next
            lenA += 1
        
        while lastB and lastB.next:
            lastB = lastB.next
            lenB += 1

        #Tail not the same therefore can't be intersection present
        if lastA != lastB:
            return None

        if lenA > lenB:
            iterations = lenA - lenB

            while iterations > 0: 
                headA = headA.next
                iterations -= 1
        else:
            iterations = lenB - lenA
            while iterations > 0:
                headB = headB.next
                iterations -= 1
        
        while headA and headB:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
