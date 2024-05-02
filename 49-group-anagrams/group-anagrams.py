class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for i in range(len(strs)):
            res = [0] * 26
            
            for l in strs[i]:
                count = ord(l) - ord('a')
                res[count] += 1

            hashmap[tuple(res)].append(strs[i])


        print(hashmap.values())

        return hashmap.values()
