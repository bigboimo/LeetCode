class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        if s[0] == '}' or s[0] == ']' or s[0] == ')':
            return False

        stack = []

        for l in s: 
            if l == '(' or l == '[' or l =='{':
                stack.append(l)
            elif stack:
                if l == ')' and stack[-1] == '(':
                    stack.pop()
                elif l == '}' and stack[-1] == '{':
                    stack.pop()
                elif l == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            else:
                return False

        return len(stack) == 0
                
                

