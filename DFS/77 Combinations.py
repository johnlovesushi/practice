class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        curr = []

        def dfs(curr, idx):
            if len(curr) == k:
                res.append(curr.copy())
                return

            for i in range(idx, n + 1):
                curr.append(i)
                dfs(curr, i + 1)
                curr.pop()

            return

        dfs(curr, 1)
        return res