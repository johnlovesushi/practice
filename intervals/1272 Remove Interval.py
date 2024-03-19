class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        arr = []
        intervals.sort()
        for interval in intervals:
            if interval[1] < toBeRemoved[0] or interval[0] > toBeRemoved[1]:  # 没有重叠
                arr.append(interval)
            else:
                if interval[0] < toBeRemoved[0]:
                    arr.append([interval[0], toBeRemoved[0]])
                if interval[1] > toBeRemoved[1]:
                    arr.append([toBeRemoved[1], interval[1]])

        return arr
