class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for i in range(len(strs)):
            anagrams[str(sorted(strs[i]))].append(strs[i])

        return list(anagrams.values())

