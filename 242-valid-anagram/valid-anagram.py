class Solution:
    def isAnagram(self, s, t): 
        if len(s) != len(t):
            return False

        sCount = {}
        tCount = {}

        for i in range(len(s)):
            sCount[s[i]] = sCount.get(s[i], 0) + 1 
            tCount[t[i]] = tCount.get(t[i], 0) + 1

        #sCount = Counter(s)
        #tCount = Counter(t)

        return sCount == tCount