class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        res = [0] * len(nums)

        for i in range(len(nums)):
            res[i] = pre
            pre = pre * nums[i]

        print(res)

        for i in reversed(range(len(nums))):
            res[i] = res[i] * post
            post = post * nums[i]
        
        print(res)
        return(res)