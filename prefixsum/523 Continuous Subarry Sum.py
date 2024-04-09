class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        have = {}
        prefixsum = 0
        have[0] = -1  # reminder: index

        for i in range(len(nums)):
            prefixsum = (prefixsum + nums[i]) % k
            if prefixsum in have and i - have[prefixsum] >= 2:
                return True
            have[prefixsum] = min(have.get(prefixsum, 1e5), i)  # 这里dict虽然不需要使用value = [],但要保持最小的index，

        return False

