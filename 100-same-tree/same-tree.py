# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.tree1 = []
        self.tree2 = []

        def dfs(root, arr):
            if not root:
                return None

            left = dfs(root.left, arr)
            right = dfs(root.right, arr)

            #Add values of root, left, and right subtree 
            arr.append(left)
            arr.append(root.val)
            arr.append(right)

            return root.val

        dfs(p, self.tree1)
        dfs(q, self.tree2)

        print(self.tree1, self.tree2)

        return self.tree1 == self.tree2

            