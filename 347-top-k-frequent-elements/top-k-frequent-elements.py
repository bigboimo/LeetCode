class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        print(counter)
        print(counter.most_common(k))
        # Extracting the k most common elements and returning only their values
        return [item for item, _ in counter.most_common(k)]
