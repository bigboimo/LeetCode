class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {k : i for i, k in enumerate(nums1)}
        print(nums1Idx)
        res = [-1] * len(nums1)
        stack = []

        for i in range(len(nums2)):

            while stack and stack[-1] in nums1Idx:
                if nums2[i] > stack[-1]:
                    numIdx = nums1Idx[stack[-1]]
                    res[numIdx] = nums2[i]
                    stack.pop()
                else:
                    break

            if nums2[i] in nums1Idx:
                stack.append(nums2[i])

        return res