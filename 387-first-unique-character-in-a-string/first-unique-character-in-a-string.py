class Solution:
    def firstUniqChar(self, s: str) -> int:
        #Minor code cleaning using counter method
        letters = Counter(s)

        print(letters)

        for i in range(len(s)):
            if letters[s[i]] == 1:
                return i

        return -1

        