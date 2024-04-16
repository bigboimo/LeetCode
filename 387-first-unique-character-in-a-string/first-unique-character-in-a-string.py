class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = Counter(s)

        print(letters)

        for i in range(len(s)):
            if letters[s[i]] == 1:
                return i

        return -1

        