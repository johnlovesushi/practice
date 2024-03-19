class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # 和数飞机一样，因为只要有一个时间段最多重合的，那么就最少需要这个数量的meeting room

        count, maxCount = 0, 0

        # 0
        # +1
        # _____5
        #     +1
        # __________10
        #           -1
        # _________________15
        #                  +1
        # _________________________20
        #                          -1
        # ____________________________________30
        #                                     -1
        arr = []
        for interval in intervals:
            arr.append((interval[0], 1))
            arr.append((interval[1], -1))
        arr.sort()

        for idx, cost in arr:
            count += cost
            maxCount = max(count, maxCount)
        return maxCount

