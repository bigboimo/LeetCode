# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        def dfs(root, maxVal):
            if not root:
                return 0

            res = 1 if root.val >= maxVal else 0
            maxVal = max(root.val, maxVal)
            res += dfs(root.right, maxVal)
            res += dfs(root.left, maxVal)
            return res
        
        return dfs(root, root.val)
