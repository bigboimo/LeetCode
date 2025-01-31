class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = Counter(s1)
        s2Count = {}
        counter = 0
        l = 0

        for r in range(len(s2)):

            s2Count[s2[r]] = s2Count.get(s2[r], 0) + 1

            if r - l + 1 > len(s1):
                s2Count[s2[l]] -= 1
                if not s2Count[s2[l]]:
                    s2Count.pop(s2[l])
                l += 1

            print(s2Count)
            if s1Count == s2Count:
                return True
        
        return False