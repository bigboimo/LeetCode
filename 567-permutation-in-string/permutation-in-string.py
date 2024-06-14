class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = Counter(s1)
        for i in range(len(s2)):
            s2Count = {}
            r = i

            if s2[i] in s1Count:
                s2Count = Counter(s2[r: r + len(s1)])
            
            print(s2Count)

            if s1Count == s2Count: 
                return True
        return False

        