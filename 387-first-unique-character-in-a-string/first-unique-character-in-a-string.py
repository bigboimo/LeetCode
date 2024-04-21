class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique = Counter(s)

        for i in range(len(s)):
            if unique[s[i]] == 1:
                return i
        
        return -1