class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        elementsCounter = Counter(nums)
        res = []
        for num, count in elementsCounter.items():
            if count > len(nums)/3:
                res.append(num)
        
        return res