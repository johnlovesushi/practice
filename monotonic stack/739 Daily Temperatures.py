class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # monotonic stack 单调递减
        res = [0] * len(temperatures)
        stack = []  # (val, idx)
        # [73]       res:[0]
        # [76] -> 73 res:[0 0]
        # [76 72]    res:[1 0 0]
        # [76 72 69] res:[1 1 0 0]
        # .....
        for i in range(len(temperatures) - 1, -1, -1):
            while stack and stack[-1][0] <= temperatures[i]: stack.pop()
            res[i] = 0 if not stack else stack[-1][1] - i
            stack.append((temperatures[i], i))

        return res
