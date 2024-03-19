class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # interval 三兄弟第一题

        arr = []
        intervals.sort()
        for interval in intervals:
            if not arr or arr[-1][1] < interval[0]:
                arr.append(interval)
            else:
                arr[-1][0] = min(arr[-1][0], interval[0])
                arr[-1][1] = max(arr[-1][1], interval[1])

        return arr
