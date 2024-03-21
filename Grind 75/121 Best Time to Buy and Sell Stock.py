class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # method 1
        # profit = 0
        # l = 0
        # for r in range(len(prices)):
        #     if prices[r] > prices[l]:
        #         profit = max(profit,prices[r]-prices[l])
        #     else:
        #         l = r

        # return profit

        # method 2
        profit = [0] * len(prices)
        hold = [0] * len(prices)
        hold[0] = -prices[0]

        for i in range(1, len(prices)):
            profit[i] = max(profit[i - 1], prices[i] + hold[i - 1])
            hold[i] = max(hold[i - 1], -prices[i])
        return profit[-1]