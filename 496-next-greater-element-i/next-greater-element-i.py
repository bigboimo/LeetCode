class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        values = {n : i for i, n in enumerate(nums1)}
        print(values)
        res = [-1] * len(nums1)


        for i in range(len(nums2)):
            if nums2[i] not in values:
                continue
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    numsIdx = values[nums2[i]]
                    res[numsIdx] = nums2[j]
                    break

        return res