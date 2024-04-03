class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # 寻找k个奇数

        # 寻找exact k 转化为最多k个奇数 - 最多k-1个奇数

        def atMostK(k):
            l = 0
            res = 0

            for r in range(len(nums)):
                if nums[r] % 2 == 1:  # 是奇数
                    k -= 1

                while k < 0:
                    if nums[l] % 2 == 1:
                        k += 1
                    l += 1
                res += r - l + 1
            return res

        return atMostK(k) - atMostK(k - 1)