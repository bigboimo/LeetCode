class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numList = []
        nums.sort()
        print(nums)

        for i in range(len(nums)): 

            if i > 0 and nums[i] == nums[i-1]: 
                continue

            L, R = i + 1, len(nums) - 1

            while L < R:
                target = nums[i] + nums[L] + nums[R]

                if target < 0: 
                    L += 1
                elif target > 0: 
                    R -= 1
                else: 
                    numList.append([nums[i], nums[L], nums[R]])
                    L += 1
                    while L < R and nums[L-1] == nums[L]: 
                        L += 1
                
        return numList
            