class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        else:
            return (3**31) % n == 0