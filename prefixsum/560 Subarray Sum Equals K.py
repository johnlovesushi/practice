class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # prefix sum

        # prefixsum = [0]*(len(nums)+1)

        # for i in range(len(nums)):
        #     prefixsum[i+1] = prefixsum[i] + nums[i] # 这里面prefixsum 第一个是0

        # count = 0
        have = {}
        have[0] = 1
        res = 0
        prefixsum = 0
        for num in nums:
            prefixsum += num
            if prefixsum - k in have: res += have[prefixsum - k]
            have[prefixsum] = have.get(prefixsum, 0) + 1

        return res


