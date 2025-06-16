class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []


        def dfs(i, curr, currSum):
            if currSum == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or currSum > target:
                return

            #Add the number to decision tree
            curr.append(candidates[i])
            dfs(i, curr, currSum + candidates[i])

            #Do not add the number to decision tree and move to the next
            curr.pop()
            dfs(i + 1, curr, currSum)
        
        dfs(0, [], 0)
        return res

     