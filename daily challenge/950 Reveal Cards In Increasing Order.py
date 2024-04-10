from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # daily challenge 2024-04-10
        deck.sort()  # 排序变成 [2, 3, 5, 7, 11, 13, 17]
        n = len(deck)
        res = [0] * n
        q = deque(range(n))

        for card in deck:
            idx = q.popleft()
            res[idx] = card  # [2, 0, 0, 0, 0, 0, 0]          deque([2, 3, 4, 5, 6, 1])
            # [2, 0, 3, 0, 0, 0, 0]          deque([4, 5, 6, 1, 3])
            # [2, 0, 3, 0, 5, 0, 0]          deque([6, 1, 3, 5])
            # [2, 0, 3, 0, 5, 0, 7]          deque([3, 5, 1])
            if q:
                q.append(q.popleft())

        return res
