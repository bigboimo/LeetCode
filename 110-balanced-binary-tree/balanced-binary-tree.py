# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True

        def depth(root):
            if not root:
                return 0
            
            left = depth(root.left)
            right = depth(root.right)
            balanced = abs(left - right) <= 1

            if not balanced:
                self.isBalanced = False

            return max(left, right) + 1

        depth(root)
        return self.isBalanced

       
        