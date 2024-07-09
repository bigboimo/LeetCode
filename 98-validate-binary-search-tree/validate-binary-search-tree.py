# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []

        def dfs(root):
            if not root:
                return None

            left = dfs(root.left)
            arr.append(root.val)
            right = dfs(root.right)

            return arr
        
        dfs(root)
        prev = arr[0] - 1
        print(arr)
        for n in arr:
            if prev >= n:
                return False
            prev = n
        
        return True
