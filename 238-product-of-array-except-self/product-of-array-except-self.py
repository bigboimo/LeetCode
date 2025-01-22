class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            print(res[i])
            pre *= nums[i]

        print(res)

        post = 1
        for i in range(len(nums) - 1, -1, -1):
            print(nums[i])
            res[i] *= post
            post *= nums[i]
            

        print(res)

        return res
