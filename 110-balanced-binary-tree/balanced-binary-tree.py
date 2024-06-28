# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True
        self.isChanged = True

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            self.isBalanced = abs(left - right) <= 1

            if not self.isBalanced:
                self.isChanged = False

            return 1 + max(right, left)

        dfs(root)
        return self.isBalanced and self.isChanged