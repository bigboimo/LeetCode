class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = {}

        for i in range(len(s)):
            letters[s[i]] = letters.get(s[i], 0) + 1

        print(letters)

        for l in s:
            if letters[l] == 1:
                return s.index(l)

        return -1

        