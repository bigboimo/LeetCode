class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        tCount = {}
        sCount = {}

        for i in range(len(s)):
            tCount[t[i]] = tCount.get(t[i], 0) + 1
            sCount[s[i]] = sCount.get(s[i], 0) + 1
            
        return tCount == sCount

