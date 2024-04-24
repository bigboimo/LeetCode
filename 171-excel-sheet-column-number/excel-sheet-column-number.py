class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        #O(1) space optimization
        strn = columnTitle[::-1]
        res = 0

        for i in range(len(strn)):
            curr = ord(strn[i]) - ord('A') + 1
            res += curr * (26**i)
            
        return res