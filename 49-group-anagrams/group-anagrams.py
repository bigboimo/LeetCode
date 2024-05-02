class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for i in range(len(strs)):
            hashmap[tuple(sorted(strs[i]))].append(strs[i])


        print(hashmap.values())

        return hashmap.values()
