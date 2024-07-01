# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = []
        self.q = []

        print(p.val)
        print(q.val)

        def dfs(root, target, arr):
            if not root:
                return 0

            if target > root.val:
                arr.append(root.val)
                dfs(root.right, target, arr)
            elif target < root.val:
                arr.append(root.val)
                dfs(root.left, target, arr)
            else:
                arr.append(root.val)
                return root.val

        dfs(root, p.val, self.p)
        dfs(root, q.val, self.q)

        print(self.p)
        print(self.q)
        
        res = []

        for i in range(min(len(self.p), len(self.q))):
            if self.p[i] == self.q[i]:
                res.append(TreeNode(self.p[i]))

        return res[-1] 


