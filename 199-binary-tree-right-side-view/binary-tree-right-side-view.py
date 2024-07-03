# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque()
        queue.append(root)
        res = []

        while queue:
            level = []

            for _ in range(len(queue)):
                currNode = queue.popleft()
                level.append(currNode)
                
                if currNode.left:
                    queue.append(currNode.left)

                if currNode.right:
                    queue.append(currNode.right)

            res.append(level[-1].val)

        return res
                