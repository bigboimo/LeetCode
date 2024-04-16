class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums)/2
        numCounter = Counter(nums)

        for i in range(len(nums)):
            if numCounter[nums[i]] > majority:
                return nums[i]
