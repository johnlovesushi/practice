class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def isValid(mid):
            total = sum([math.ceil(num / mid) for num in nums])

            # print(total,threshold)
            return total <= threshold

        l, r = 0, max(nums)

        while l + 1 < r:
            mid = l + (r - l) // 2
            # print(l,r,mid)
            if isValid(mid):  # 合格的，但有可能过大
                r = mid
            else:
                l = mid

        return r
