class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minVal = nums[l] 

        while l <= r:
            
            mid = (l+r)//2
            minVal = min(minVal, nums[mid])

            #This statement verifies that we're going in increasing order and mid is more then r meaning we're in the unsorted portion
            if nums[mid] >= nums[l] and nums[mid] > nums[r]:
                l = mid + 1
            else: 
                r = mid - 1

        return minVal