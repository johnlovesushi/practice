class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums) - 1
        r = sum(nums)
        res = r

        while l + 1 < r:
            mid = l + (r - l) // 2
            if self.canSplit(mid, nums, k):  # 说明可以得到这个数值
                res = mid
                r = mid
            else:  # 说明不可以得到这个数值
                l = mid
        return res

    def canSplit(self, mid, nums, m):
        subarry = 0
        curSum = 0
        for n in nums:
            curSum += n
            if curSum > mid:
                curSum = n
                subarry += 1

        return subarry + 1 <= m 