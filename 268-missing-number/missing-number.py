class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #O(n) time and constant space solution using sum formula
        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i])
            print(res)
        
        return res
