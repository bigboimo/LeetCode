class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Moore's voting algorithm O(n) time and O(1) space
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            count += 1 if res == n else -1
        
        return res