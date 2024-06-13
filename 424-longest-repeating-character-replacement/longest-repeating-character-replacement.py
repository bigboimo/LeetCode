class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lCount = {}
        res = 0
        l = 0
        mostf = 0

        for r in range(len(s)):
            lCount[s[r]] = 1 + lCount.get(s[r], 0)
            mostf = max(mostf, lCount[s[r]])
            
            while (r - l + 1) - mostf > k:
                lCount[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
