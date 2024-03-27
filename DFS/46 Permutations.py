class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        visited = set()
        curr = []

        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                if nums[i] in visited: continue
                visited.add(nums[i])
                curr.append(nums[i])
                dfs(curr)
                curr.pop()
                visited.remove(nums[i])

            return

        dfs(curr)
        return res