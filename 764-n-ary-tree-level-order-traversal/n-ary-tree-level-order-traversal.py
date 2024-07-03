"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        queue.append([root])
        res = []


        #bfs
        while queue:
            nodes = []

            for _ in range(len(queue)):
                currNode = queue.popleft()

                if currNode:
                    for n in currNode:
                        nodes.append(n.val)
                        queue.append(n.children)
            if nodes:
                res.append(nodes)

        return res