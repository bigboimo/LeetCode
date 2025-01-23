class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(numbers) - 1

        while l > -1 and r < len(numbers):

            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else: 
                return [l + 1, r + 1]