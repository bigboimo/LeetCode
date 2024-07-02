class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1Count = Counter(nums1)
        num2Count = Counter(nums2)
        
        res = []
        
        for num in num1Count:
            if num in num2Count:
                min_count = min(num1Count[num], num2Count[num])
                res.extend([num] * min_count)
                
        return res

