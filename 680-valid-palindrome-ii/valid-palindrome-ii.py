class Solution:
    #O(n) time and O(1) space optimize since list comprehension wasn't used
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            
            if s[l] != s[r]:
                return (self.isPalindrome(s, l + 1, r) or self.isPalindrome(s, l, r - 1))


            l += 1
            r -= 1
        
        return True

    
    def isPalindrome(self, s, l, r):
        
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True

            