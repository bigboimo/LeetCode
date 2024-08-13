class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}

        for i in range(len(nums)):

            if nums[i] in sums:
                return [sums[nums[i]], i]
                
            key = target - nums[i]
            sums[key] = i