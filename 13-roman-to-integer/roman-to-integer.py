class Solution:
    def romanToInt(self, s: str) -> int:
        mapRom = {'I':1, 'V':5, 'X':10, 'L':50, 'C': 100, 'D':500, 'M': 1000}
        res = 0
        prev = None

        for i in range(len(s)):
            
            res += mapRom[s[i]]

            if prev == 'I' and (s[i] == 'V' or s[i] == 'X'):
                res -= 1*2
            elif prev == 'X' and (s[i] == 'L' or s[i] == 'C'):
                res -= 10*2
            elif prev == 'C' and (s[i] == 'D' or s[i] == 'M'):
                res -= 100*2

            prev = s[i]

        return res