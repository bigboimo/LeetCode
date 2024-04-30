class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #O(m * n) optimized solution
        hashmap = defaultdict(list)
        

        for l in strs:
            res = [0] * 26 
            
            for s in l:
                count = ord(s) - ord('a') 
                res[count] += 1
            
            hashmap[tuple(res)].append(l)

        return hashmap.values()


