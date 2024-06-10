class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r)//2

            print(l, mid, r)

            if nums[mid] == target:
                return mid

            #left-sorted side
            if nums[mid] >= nums[l]:
                print('left')
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else: 
                    l = mid + 1
            #right-sorted side
            else:
                print('right')
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else: 
                    r = mid - 1
            

        return -1

