class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        added = set()
        res = 0
        r = 0

        for l in range(len(s)):
            while s[l] in added:
                added.discard(s[r])
                r += 1
                print(added)
            added.add(s[l])
            res = max(len(added), res)
            
            
            
        return res


            
