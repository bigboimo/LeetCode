"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = { None: None }
        
        cur = head
        while cur:
            newNode = Node(cur.val)
            oldToNew[cur] = newNode
            cur = cur.next
        
        cur = head
        while cur:
            newNode = oldToNew[cur]
            newNode.next = oldToNew[cur.next]
            newNode.random = oldToNew[cur.random]
            
            cur = cur.next
        
        return oldToNew[head]