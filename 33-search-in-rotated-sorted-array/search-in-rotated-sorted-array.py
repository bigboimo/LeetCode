class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        pivot = l
        res = -1

        #Modified binary search to find pivot point (lowest number)
        while l <= r:
            mid = (l+r)//2

            pivot = mid
            if nums[mid] >= nums[l] and nums[mid] > nums[r]:
                l += 1
            else:
                r -= 1

        l, r = 0, len(nums) - 1

        #Find our number based on target
        if target >= nums[pivot] and target <= nums[-1]:
            l = pivot
        else: 
            r = pivot - 1
        
        #Unmodified binary search implementation
        while l <= r:
            mid = (l+r)//2

            if nums[mid] < target:
                l += 1
            elif nums[mid] > target:
                r -= 1
            else:
                res = mid
                break
        return res
