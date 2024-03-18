import heapq
class FreqStack:
    # 方法一：使用priorityqueue 来记录，按照<freq,pushCount,val>
    # 来排序
    def __init__(self):
        self.cnt = {}
        self.pq = []
        self.pushCount = 0

    def push(self, val: int) -> None:  # 因为是minheap, 所以只能都是负的来保证pop出来的是最大的
        self.cnt[val]= 1 + self.cnt.get(val,0)
        self.pushCount+=1
        heapq.heappush(self.pq, [-self.cnt[val], -self.pushCount, val])

    def pop(self) -> int:
        cnt, freq, val = heapq.heappop(self.pq)
        self.cnt[val]-=1
        #print(cnt,freq,val)
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()


class FreqStack:
    # 方法二：使用两个map记录
    # map1 来存<val,freq>; map2来存 <maxCount, [val1,val2, ...]>
    # 每次pop从maxCount里面的list开始pop
    def __init__(self):
        self.cnt = {}
        self.maxCnt = {}  # 这个用来记录最大frequency下面有哪些元素，按照顺序排序进去，最后pop出来
        self.maxCount = 0

    def push(self, val: int) -> None:
        self.cnt[val] = 1 + self.cnt.get(val, 0)  # 先保存当前数值val的freq
        cur_cnt = self.cnt[val]
        if cur_cnt > self.maxCount:  # 更新了最大maxCount
            self.maxCnt[cur_cnt] = []  # 创建一个新的list用来存储
            self.maxCount = cur_cnt

        self.maxCnt[cur_cnt].append(val)  # 无论是不是maxCount，都需要更新freq,然后存储当前freq下面的list,这个list会有顺序功能

    def pop(self) -> int:
        val = self.maxCnt[self.maxCount].pop()
        self.cnt[val] -= 1  # note: 每一次pop完之后需要更新原始的map里面的freq,因为下一次再进入相同元素，不会从其原来历史最大freq来计数
        if not self.maxCnt[self.maxCount]:  # 如果当前maxCount空了，那么说明没有这个maxCount的数值了，那么maxCount需要--
            self.maxCount -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()