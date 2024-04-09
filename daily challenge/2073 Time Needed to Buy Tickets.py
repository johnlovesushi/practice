class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        res = 0

        for i in range(len(tickets)):
            if i <= k:
                res += min(tickets[i], tickets[k])
            else:  # 因为tickets[k]到最后一张买完后，后面所有的就不会再继续买票
                res += min(tickets[i], tickets[k] - 1)

        return res
