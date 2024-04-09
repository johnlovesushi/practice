class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        # 暴力求解 O(n^2) time limit exceeded
        # res = 0
        # for end in range(len(nums)):
        #     zeros, ones = 0,0
        #     for start in range(end, len(nums)):          # 包含当前start的值
        #         if nums[start] == 0:
        #             zeros+=1
        #         else:
        #             ones+=1

        #         if zeros == ones:
        #             res = max(res,ones + zeros)

        # return res

        # prefix sum
        # 先把0都变成-1
        for i in range(len(nums)):
            if nums[i] == 0: nums[i] = -1

        have = {}
        res = 0
        prefixsum = 0
        have[0] = -1
        for i in range(len(nums)):
            prefixsum += nums[i]
            if prefixsum in have:  # 两个prefixsum 的值相同，那么的差就一定为0，说明差值(subarray)有相同数量的0和1
                res = max(res, i - have[prefixsum])

            have[prefixsum] = min(have.get(prefixsum, 1e5), i)

        return res


