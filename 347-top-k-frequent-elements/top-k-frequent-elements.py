class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCounts = Counter(nums)
        topKnums = [ [] for i in range(len(nums) + 1) ] 
        added = set()
        for i in range(len(nums)):
            if nums[i] in added:
                continue
            counts = freqCounts[nums[i]]
            print(counts)
            topKnums[counts - 1].append(nums[i])
            added.add(nums[i])

        print(topKnums)
        res = []

        for i in reversed(range(len(topKnums))):
            print(topKnums[i])
            if len(res) < k and topKnums[i]:
                res += topKnums[i]
        
        print(res)

        return res