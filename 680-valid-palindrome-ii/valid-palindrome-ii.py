class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            
            if s[l] != s[r]:
                skipL, skipR = s[l + 1 : r + 1], s[l : r]

                return (skipL[::-1] == skipL) or skipR[::-1] == skipR


            l += 1
            r -= 1
        
        return True

    

            