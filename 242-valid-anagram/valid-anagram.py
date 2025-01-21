class Solution:
    def isAnagram(self, s, t): 
        if len(s) != len(t):
            return False

        sCount = Counter(s)
        tCount = Counter(t)

        return sCount == tCount