class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # method 1
        '''
        理解上方法一和方法二是一样的，只不过方法一用了一个currMax来记录过程当中的最大值，但是方法二是在dp arr里面取到最大值
        :param nums:
        :return:
        '''
        if len(nums) == 1: return nums[0]
        dp = [0]* len(nums)
        dp[0] = (nums[0])
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])

        return max(dp)

        # method 2
        currMax, curr = -float("infinity"), -float("infinity")

        for i in range(len(nums)):
            curr = max(nums[i], curr + nums[i])
            currMax = max(curr, currMax)

        return currMax


