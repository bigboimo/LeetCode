class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        num = (-math.inf)
        powr = 0

        while num < n:
            num = 3 ** powr
            
            if num == n:
                return True
            
            powr += 1
        
        return False