class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perm = Counter(s1)

        for i in range(len(s2)):
            if s2[i] in perm:
                new = Counter(s2[i:i+len(s1)])
                print(new)
                if new == perm:
                    return True

        return False