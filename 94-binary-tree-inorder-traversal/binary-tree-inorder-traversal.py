# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Iterative inorder DFS
        res = []
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res
        
        
        
        #Inorder DFS recursive
        def dfs(root, list):
            if not root:
                return None

            dfs(root.left, nodeList)
            nodeList.append(root.val)
            dfs(root.right, nodeList)

            return nodeList

        nodeList = []
        return dfs(root, nodeList)
        


        