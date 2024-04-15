# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return [True, 0]
            
            #Recursively call left and right subtrees
            left, right = dfs(root.left), dfs(root.right)
            #Boolean to check if every subtree hold True for balanced and the height diff is <= 1
            balanced = right[0] and left[0] and abs(left[1] - right[1]) <= 1
            
            return [balanced, max(left[1], right[1]) + 1]
        
        return dfs(root)[0]

       

            

            