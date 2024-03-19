class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intervals = firstList + secondList
        intervals.sort()

        arr = []
        intersection = []

        for interval in intervals:
            if not arr or arr[-1][1] < interval[0]:
                arr.append(interval)
            else:  # 有 intersection
                # 判断intersection and add into
                overlap_start = max(arr[-1][0], interval[0])
                overlap_end = min(arr[-1][1], interval[1])
                intersection.append([overlap_start, overlap_end])

                arr[-1][0] = min(arr[-1][0], interval[0])
                arr[-1][1] = max(arr[-1][1], interval[1])
        return intersection

