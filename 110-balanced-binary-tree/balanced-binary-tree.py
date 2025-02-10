# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def depth(root):
            if not root:
                return 0
            
            left = depth(root.left)
            right = depth(root.right)

            return max(left, right) + 1


        if not root:
            return True
        
        left = depth(root.left)
        right = depth(root.right)

        balanced = abs(left - right) <= 1
        return balanced and self.isBalanced(root.left) and self.isBalanced(root.right)

       
        