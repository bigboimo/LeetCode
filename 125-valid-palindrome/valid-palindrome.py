class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for l in s: 
            if l.isalnum():
                newStr +=l.lower()
        print(newStr)
        print(newStr[::-1])
        return newStr == newStr[::-1]
