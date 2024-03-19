"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # 和数飞机那个差不太多，只有count=0的时候，就说明可能有空隙然后我们需要记录，然后count不再变成0，那么我们就得记录end time
        record = False
        count = 0
        arr = []
        start, end = 0, 0
        res = []
        for personal_schedule in schedule:
            for interval in personal_schedule:
                arr.append((interval.start, 1))
                arr.append((interval.end, -1))
        arr.sort()
        # print(arr)
        for val, cost in arr:
            count += cost
            if count == 0 and record == False:  # 记录开始时间
                start = val
                record = True
            if count != 0 and record == True:  # count不再是0，并且原来是在record,那么记录到结果当中
                end = val
                record = False
                if end > start:
                    res.append(Interval(start, end))
            # print(count,val,record)
        return res
