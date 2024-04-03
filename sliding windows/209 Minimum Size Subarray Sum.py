class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total_sum = 0
        res = float("infinity")
        for r in range(len(nums)):
            total_sum += nums[r]

            while total_sum >= target:
                res = min(res, r - l + 1)

                # 满足条件后可以往左移动直到不再满足条件
                total_sum -= nums[l]
                l += 1

        return 0 if res == float("infinity") else res

