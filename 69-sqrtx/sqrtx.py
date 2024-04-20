class Solution:
    def mySqrt(self, x: int) -> int:
        #Binary search O(logn) solution
        res = 0

        l, r = 0, x

        while l <= r:
            #Overflow protection
            mid = l + (r - l)//2

            if mid*mid < x:
                l = mid + 1
                res = mid
            elif mid*mid > x:
                r = mid - 1
            else:
                return mid
        return res

        