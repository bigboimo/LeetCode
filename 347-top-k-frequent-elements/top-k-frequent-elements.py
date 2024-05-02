class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]

        for n, c in counter.items():
            freq[c].append(n)

        print(freq)

        ret = []

        for i in reversed(range(len(freq))):
            for n in freq[i]:
                print(freq[i])
                ret.append(n)
                if len(ret) >= k:
                    return ret
