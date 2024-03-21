class Solution:
    @cache
    def climbStairs(self, n: int) -> int:

        # method 1: iteration
        if n == 1: return 1
        if n == 2: return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)

        # method 2: 
        if n == 1: return 1
        if n == 2: return 2
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]
