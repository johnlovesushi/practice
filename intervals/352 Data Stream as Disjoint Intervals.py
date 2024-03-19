class SummaryRanges:

    # 每次需要getIntervals的时候，再生成interval return 出去
    def __init__(self):
        self.nums = set()

    def addNum(self, value: int) -> None:
        self.nums.add(value)

    def getIntervals(self) -> List[List[int]]:
        visited = set()
        res = []
        for val in self.nums:
            if val in visited:  # 如果已经被使用了，那么直接跳过
                continue

            left = val
            while left in self.nums:
                visited.add(left)
                left -= 1

            right = val
            while right in self.nums:
                visited.add(right)
                right += 1

            # 找到了这个区间然后不再循环，那么可以生成interval了
            res.append([left + 1, right - 1])
        return sorted(res)

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()