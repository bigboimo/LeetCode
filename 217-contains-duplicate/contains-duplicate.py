class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup = set()

        for i in range(len(nums)):
            if nums[i] in dup: 
                return True
            dup.add(nums[i])
        return False