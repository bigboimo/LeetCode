class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        p = [-1 if x == 0 else 1 for x in possible]

        left, right = 0, sum(p)

        for i in range(len(p) - 1):
            left += p[i]
            right -= p[i]

            if left > right:
                return i + 1
        
        return -1


        
           


