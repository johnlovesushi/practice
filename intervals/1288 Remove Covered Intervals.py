class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        arr = []
        intervals.sort(key = lambda x: (-x[0],x[1]))
        # 第一个index够小才能够覆盖，所以排序是按照[0] 的降序，但是[1]的增序
        for interval in intervals:
            print(interval)
            while arr and (arr[-1][0] >= interval[0] and arr[-1][1] <= interval[1]):
                arr.pop()

            arr.append(interval)
            #print(arr)
        return len(arr)