class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def atMostK(K):  # 最多有K个完全不一样的元素
            l = 0
            have = {}
            res = 0
            for r in range(len(nums)):
                if have.get(nums[r], 0) == 0: K -= 1
                have[nums[r]] = 1 + have.get(nums[r], 0)

                while K < 0:
                    have[nums[l]] -= 1
                    if have[nums[l]] == 0: K += 1
                    l += 1

                res += r - l + 1

            return res

        return atMostK(k) - atMostK(k - 1)