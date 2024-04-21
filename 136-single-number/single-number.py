class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 #n ^ 0 = n

        for n in nums:
            res = n ^ res
        
        return res
        
        