class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()

        arr = []

        for interval in intervals:
            if not arr or arr[-1][1] < interval[0]:
                arr.append(interval)
            else:
                arr[-1][0] = min(arr[-1][0],interval[0])
                arr[-1][1] = max(arr[-1][1],interval[1])

        return arr                