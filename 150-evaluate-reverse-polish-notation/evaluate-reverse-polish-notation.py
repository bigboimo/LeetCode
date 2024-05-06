class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:

            if t == '+':
                curr = stack.pop()
                prev = stack.pop()
                stack.append(prev + curr) 
            elif t == '-':
                curr = stack.pop()
                prev = stack.pop()
                stack.append(prev - curr) 
            elif t == '*':
                curr = stack.pop()
                prev = stack.pop()
                stack.append(prev * curr) 
            elif t == '/':
                curr = stack.pop()
                prev = stack.pop()
                stack.append(int(prev/curr))
            else:
                stack.append(int(t))

        print('outside loop')
        print(stack)
        return stack[-1]
