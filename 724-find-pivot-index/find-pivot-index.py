class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)

        res = 0
        for i in range(1, len(nums)):
            res += nums[i - 1]
            prefix[i] = res
        
        print(prefix)

        res = 0
        for i in range(len(nums) - 2, -1, -1):
            res += nums[i + 1]
            postfix[i] = res
        
        for i in range(len(nums)):
            if prefix[i] == postfix[i]:
                return i

        return -1
