class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = defaultdict(list)

        for s in strs: 
            counter[tuple(sorted(s))].append(s)

        return counter.values()