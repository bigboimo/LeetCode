class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[l]

        while l<= r:
            mid =(l+r)//2

            #res = min(nums[mid], res)
            res = nums[mid]
            if nums[mid] >= nums[l] and nums[mid] > nums[r]:
                l += 1
            else: 
                r -= 1

        return res