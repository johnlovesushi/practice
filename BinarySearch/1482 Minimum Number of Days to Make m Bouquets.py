class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        if len(bloomDay) < m * k: return -1

        def isValid(mid):
            count = 0
            temp = 0
            for day in bloomDay:
                if day <= mid:
                    temp += 1
                else:
                    temp = 0

                if temp >= k:
                    count += 1
                    temp = 0
            return count >= m

        l, r = 0, max(bloomDay)

        while l + 1 < r:

            mid = l + (r - l) // 2
            # print(l,r,mid)
            if isValid(mid):  # 如果可以成功，缩小
                r = mid
            else:
                l = mid

        return r

