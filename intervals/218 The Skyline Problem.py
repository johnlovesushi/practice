import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        arr = []
        for building in buildings:
            arr.append([building[0], building[2]])
            arr.append([building[1], -building[2]])
        pq = [0]
        res = []
        arr.sort(key=lambda x: (x[0], -x[1]))
        print(arr)
        for idx, val in arr:
            if val > 0:  # 说明有新的大楼进来
                # 如果刷新高度，那么加入一个点
                if val > abs(pq[0]):
                    heapq.heappush(pq, -val)
                    res.append([idx, -pq[0]])
                else:
                    heapq.heappush(pq, -val)
            else:  # 有大楼影子结束了
                pq.remove(val)
                heapq.heapify(pq)
                if val < pq[0]:  # 就是最高大楼的影子，那么需要插入一个新的， 如果不是最高的，那么不需要插入新的点，直接remove高度就可以了
                    res.append([idx, -pq[0]])

        return res
