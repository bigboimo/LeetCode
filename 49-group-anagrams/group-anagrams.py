class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = defaultdict(list)

        for i in range(len(strs)):
            curr = ''.join(sorted(strs[i]))
            hashmap[curr].append(strs[i])

        return hashmap.values()

            
