class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}

        for i in range(len(nums)):
            res = target - nums[i]

            if nums[i] in tracker:
                return [tracker[nums[i]] , i] 

            tracker[res] = i
