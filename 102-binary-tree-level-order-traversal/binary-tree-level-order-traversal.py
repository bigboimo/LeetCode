# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []

        def bfs(root):
            if not root: 
                return self.res 

            queue = deque()
            queue.append(root)

            while queue:
                nodes = []
                for _ in range(len(queue)):
    
                    currNode = queue.popleft()
                    nodes.append(currNode.val)

                    if currNode.left:
                        queue.append(currNode.left)
                    
                    if currNode.right:
                        queue.append(currNode.right)
                self.res.append(nodes)
            
            print(self.res)
            return self.res
        
        return bfs(root)



        