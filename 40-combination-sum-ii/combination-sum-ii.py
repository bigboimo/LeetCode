class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)

        def dfs(i, curr, currSum):
            if currSum == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or currSum > target: 
                return 
            
            #Add number to decision tree
            curr.append(candidates[i])
            dfs(i + 1, curr, currSum + candidates[i])

            #Do not add number to decision tree
            curr.pop()
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curr, currSum)

        dfs(0, [], 0)
        return res