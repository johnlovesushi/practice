class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # 和数飞机一样，因为只要有一个时间段最多重合的，那么就最少需要这个数量的meeting room
        # method 1 普通扫描线
        count,maxCount = 0,0

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
            arr.append((interval[0],1))
            arr.append((interval[1],-1))
        arr.sort()

        for idx,cost in arr:
            count+= cost
            maxCount = max(count, maxCount)
        return maxCount

        # method 2: pq 做法
        pq = []
        intervals.sort()
        for interval in intervals:
            if pq and pq[0] <= interval[0]:
                heapq.heappop(pq)
            heapq.heappush(pq,interval[1])

        return len(pq)

        # method 3: 变种扫描线
        starts, ends = [], []
        for interval in intervals:
            starts.append(interval[0])
            ends.append(interval[1])

        starts.sort()
        ends.sort()
        end = 0
        room = 0
        for i in range(len(starts)):
            room += 1
            if starts[i] >= ends[end]:
                end += 1
                room -= 1

        return room