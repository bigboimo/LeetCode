class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minStack.append(val)

        if len(self.minStack) > 1 and self.minStack[-1] > self.minStack[-2]:
            self.minStack.pop()


    def pop(self) -> None:
        if self.minStack[-1] == self.stack[-1]:
            self.stack.pop()
            self.minStack.pop()
        else:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()