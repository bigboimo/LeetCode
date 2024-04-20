class Solution:
    def isPalindrome(self, s: str) -> bool:
        #O(n) time complexity
        newStr = [x.lower() for x in s if x.isalnum()]

        print(newStr)
        print(newStr[::-1])

        return newStr == newStr[::-1]