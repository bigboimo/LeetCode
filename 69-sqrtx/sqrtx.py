class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0

        while l<=r:
            mid = l + (r - l)//2

            if mid*mid < x:
                res = mid
                l = mid + 1
            elif mid*mid > x:
                r = mid - 1
            else: 
                return mid

        return res