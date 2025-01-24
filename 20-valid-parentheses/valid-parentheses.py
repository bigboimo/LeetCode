class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []

        for i in range(len(s)):

            valid = len(brackets) > 0 and ((s[i] == ')' and brackets[-1] == '(') or (s[i] == ']' and brackets[-1] == '[') or (s[i] == '}' and brackets[-1] == '{')) 
            if valid:
                brackets.pop()
                continue

            brackets.append(s[i])

        return len(brackets) == 0