class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:

        intervals = slots1 + slots2
        intervals.sort()
        arr = []
        #print(intervals)
        for interval in intervals:
            if not arr or arr[-1][1] < interval[0]:             # 没有overlap
                arr.append(interval)
            else:           # 可以来判断是否有足够的时间
                overlap_start = max(arr[-1][0], interval[0])
                overlap_end = min(arr[-1][1], interval[1])
                #print(arr)
                #print(overlap_end, overlap_start)
                if overlap_end - overlap_start >= duration: # 超过了需要的duration
                    return([overlap_start, overlap_start + duration])
                else:                                       # 时间不够
                    arr[-1][0] = min(arr[-1][0], interval[0])
                    arr[-1][1] = max(arr[-1][1], interval[1])
        return []