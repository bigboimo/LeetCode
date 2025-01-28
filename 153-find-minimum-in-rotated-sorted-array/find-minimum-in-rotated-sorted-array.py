class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[l]

        while l <= r:
            mid = (l+r)//2
            print(nums[l], nums[mid], nums[r])

            res = min(res, nums[mid])
            print(res)
            if nums[mid] >= nums[l] and nums[mid] > nums[r]:
                l = mid + 1
            else: 
                r = mid - 1
        
        return res

            