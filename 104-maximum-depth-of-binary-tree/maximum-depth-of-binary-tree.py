# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root: 
            return 0

        def bfs(root):
            #Create queue and initialize with root
            queue = deque()
            queue.append(root)
            level = 0

            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()

                    if node.right:
                        queue.append(node.right)
                    if node.left:
                        queue.append(node.left)

                level += 1

            return level

        return bfs(root)

        