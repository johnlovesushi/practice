class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        def isGood(mid):
            start = -1e100
            count = 0
            for pos in position:
                if pos - start >= mid:
                    count += 1
                    start = pos
                # print(pos-start,mid,count)
            return count >= m

        position.sort()
        l, r = 1, max(position)
        while l + 1 < r:
            mid = l + (r - l) // 2

            if isGood(mid):  # 说明m可以，那么需要取右边
                l = mid
            else:
                r = mid  #
            # print(l,mid,r)
        return l