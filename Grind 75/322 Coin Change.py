class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # method 1: dp
        dp = [float("infinity") for _ in range(amount + 1)]

        dp[0] = 0  # amount是0的时候，不需要任何coin

        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if i >= coins[j]:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)  # 确保当前的amount是大于等于coins[j]的

        return dp[-1] if dp[-1] != float("infinity") else -1