class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        mostFreq = 0
        l, r = 0, 0
        res = 0 

        while r < len(s):
            counts[s[r]] = counts.get(s[r], 0) + 1

            mostFreq = max(counts[s[r]] , mostFreq)

            while (r - l + 1) - mostFreq > k:
                counts[s[l]] = counts[s[l]] - 1
                l += 1
            
            
            res = max(res, r - l + 1) 
            r += 1

        return res
            