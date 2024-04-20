class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        integers = set(nums)
        missingNum = len(nums)

        for i in range(len(integers)):
            if i not in integers:
                missingNum = i
                break

        return missingNum 
