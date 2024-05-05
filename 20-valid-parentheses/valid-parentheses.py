class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for l in s:
            if stack and l != '{' and l != '(' and l != '[': 
                if l == '}' and stack[-1] == '{':
                    stack.pop()
                elif l == ')' and stack[-1] == '(':
                    stack.pop()
                elif l == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(l) 

        return len(stack) == 0

