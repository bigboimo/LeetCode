class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        minVal = nums[l]
        index = 0

        res = -1

        #Find minimum value in logn
        while l <= r:
            mid = (l+r) // 2
            
            if nums[mid] < minVal:
                minVal = nums[mid]
                index = mid
                
            #Check if in sorted region or not
            if nums[mid] >= nums[l] and nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1

        print(minVal)

        #Typical binary search

        if nums[index] <= target <= nums[-1]:
            l, r = index, len(nums) - 1
        else:
            l, r = 0, index - 1


        while l <= r:
            mid = (l+r)//2
            print(nums[l], nums[mid], nums[r])

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else: 
                return mid
        
        return res
            


