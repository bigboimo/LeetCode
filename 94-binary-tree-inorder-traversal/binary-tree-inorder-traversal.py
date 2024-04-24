# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Inorder DFS
        def dfs(root, list):
            if not root:
                return None

            dfs(root.left, nodeList)
            nodeList.append(root.val)
            dfs(root.right, nodeList)

            return nodeList

        nodeList = []
        return dfs(root, nodeList)
        


        