class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [nums[i] for i in range(len(nums))]
        post = [nums[i] for i in range(len(nums))]

        n = nums[0]
        for i in range(1 ,len(nums)):
            pre[i] = n * nums[i]
            n = pre[i]

        n = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            post[i] = n * post[i]
            n = post[i]

        print(pre)
        print(post)

        res = [1] * len(nums)

        print(res)

        for i in range(len(nums)):
            if (i - 1) > -1:
                res[i] *= pre[i - 1]
            if (i + 1) < len(nums):     
                res[i] *= post[i + 1] 

        return res