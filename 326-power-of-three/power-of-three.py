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

        ## Mathematical approach since upper bound is 2^31 - 1 and 3^20 is larger, if n
        ## is a power of three then it will divide without decimals which is why modulo
        ## works perfectly. 
        ## return n > 0 and 3**20 % n == 0