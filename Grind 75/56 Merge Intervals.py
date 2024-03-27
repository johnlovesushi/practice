class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        stk = []

        for interval in intervals:
            if not stk or stk[-1][1] < interval[0]:
                stk.append(interval)
            else:
                stk[-1][0] = min(stk[-1][0], interval[0])
                stk[-1][1] = max(stk[-1][1], interval[1])

        return stk