class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        prevNums = set()

        for i in range(len(nums)):
            if nums[i] in prevNums:
                return True
            prevNums.add(nums[i])

        return False 