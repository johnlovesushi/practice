class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr = []
        res = []

        def dfs(idx, curr):
            res.append(curr.copy())

            for i in range(idx, len(nums)):
                curr.append(nums[i])
                dfs(i + 1, curr)  # 在这里进行index的加法
                curr.pop()

            return

        dfs(0, curr)
        return res