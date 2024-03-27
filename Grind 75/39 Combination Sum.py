class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # dfs
        res = []
        curr = []
        n = len(candidates)

        def dfs(idx, curr, reminder):
            if reminder == 0:
                res.append(curr.copy())
                return

            for i in range(idx, n):
                if candidates[i] > reminder:
                    continue

                curr.append(candidates[i])
                dfs(i, curr, reminder - candidates[i])
                curr.pop()
            return

        dfs(0, curr, target)
        return res