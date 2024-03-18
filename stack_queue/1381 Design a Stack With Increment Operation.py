class CustomStack:

    def __init__(self, maxSize: int):
        self.stk = []
        self.size = 0
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if self.size != self.maxSize:
            self.stk.append(x)
            self.size+=1

    def pop(self) -> int:
        if self.size == 0: return -1
        else:
            self.size-=1
            return self.stk.pop()

    def increment(self, k: int, val: int) -> None:
        if self.size !=0:
            min_val = min(k,self.size)
            for i in range(min_val):
                self.stk[i]+=val
        return


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)