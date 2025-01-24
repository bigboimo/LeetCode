class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []

        for token in tokens:
            if token in "+-*/":
                # Pop two numbers from the stack
                b = numStack.pop()
                a = numStack.pop()

                # Perform the operation
                if token == "+":
                    numStack.append(a + b)
                elif token == "-":
                    numStack.append(a - b)
                elif token == "*":
                    numStack.append(a * b)
                elif token == "/":
                    # Correctly handle truncation towards zero
                    numStack.append(int(a / b))
            else:
                # Push numbers onto the stack
                numStack.append(int(token))

        # The last element in the stack is the result
        return numStack.pop()