class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # 寻找余数相同的情况
        have = {}
        res = 0
        prefixsum = 0
        have[0] = 1
        for num in nums:
            prefixsum = (prefixsum + num) % k
            res += have.get(prefixsum, 0)
            have[prefixsum] = have.get(prefixsum, 0) + 1

        return res

