class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        substring = set()

        while r < len(s):

            while s[r] in substring:
                substring.remove(s[l])
                l += 1

            

            substring.add(s[r])
            print(substring)
            res = max(res, len(substring))
            r += 1 

        return res
