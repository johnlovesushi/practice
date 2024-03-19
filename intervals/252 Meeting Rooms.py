class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        # 方法一
        count,maxCount = 0,0
        arr = []

        for interval in intervals:
            arr.append((interval[0],1))
            arr.append((interval[1],-1))
        arr.sort()
        for idx, cost in arr:
            count+=cost
            maxCount = max(count,maxCount)
            #print(idx,count)
        return maxCount<=1

        # 方法二

        intervals.sort(key = lambda x: x[0])
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                    # 如果这一节课的结束时间大于下一节课的开始时间，那么就不可能参与所有会议
                    return False
        return True