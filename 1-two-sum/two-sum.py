class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSum = {}
        res = []

        for i in range(len(nums)):
            val = target - nums[i]

            if nums[i] in twoSum:
                res.append(twoSum[nums[i]])
                res.append(i)
                break 

            twoSum[val] = i

        return res