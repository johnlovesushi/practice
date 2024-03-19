class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        arr = []
        intervals.sort(key = lambda x: (x[1],x[1]-x[0]))

        for interval in intervals:
            if not arr or arr[-1][1] <= interval[0]:
                arr.append(interval)
        return len(intervals) - len(arr)