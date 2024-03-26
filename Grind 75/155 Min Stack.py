class MinStack:

    def __init__(self):
        self.minstk = []

    def push(self, val: int) -> None:
        if not self.minstk:
            self.minstk.append([val,val])
            return
        else:
            min_element = self.minstk[-1][1]
            self.minstk.append([val, min(val, min_element)])
    def pop(self) -> None:
        self.minstk.pop()

    def top(self) -> int:
        return self.minstk[-1][0]

    def getMin(self) -> int:
        return self.minstk[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()