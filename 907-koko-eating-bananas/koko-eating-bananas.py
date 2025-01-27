class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            mid = (l+r)//2
            
            totalTime = 0
            for i in range(len(piles)):
                totalTime += math.ceil(piles[i]/mid)
            
            if totalTime <= h:
                res = mid
            print(totalTime, l, mid, r)
            if totalTime > h:
                l = mid + 1
            else:
                r = mid - 1

        return res
