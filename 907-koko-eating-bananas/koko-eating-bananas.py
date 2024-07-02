class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        maxNum = r
        res = 0

        while l<=r: 
            mid = (l+r)//2
            print(l,mid ,r)
            timeTaken = 0

            for n in piles:
                timeTaken += math.ceil(n/mid)
            
            print(timeTaken)
            if timeTaken <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1


        return res
