class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {   '}' : '{',
                    ')' : '(',
                    ']' : '['}
        
        stack = []

        for l in s: 
            if l in pairs:
                if stack and stack[-1] == pairs[l]:
                    stack.pop()
                else: 
                    return False
            else: 
                stack.append(l)

        return len(stack) == 0
