class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minVal = nums[l] 

        while l <= r:
            mid = (l+r)//2
            minVal = min(minVal, nums[mid])
            print(nums[l], nums[mid], nums[r], minVal, 'first')


            #Sorted region 
            if nums[l] < nums[r]:
                return nums[l]


            #Unsorted region
            else:
                print(nums[l], nums[mid], nums[r])
                #Compare if array is decreasing or increasing
                if nums[mid] >= nums[l]:
                    l = mid + 1
                else:
                    r = mid
            

        return minVal