class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        visited = set()
        res = []
        curr = []

        # dfs

        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                if nums[i] in visited: continue
                curr.append(nums[i])
                visited.add(nums[i])
                dfs(curr)
                curr.pop()
                visited.remove(nums[i])
            return

        dfs(curr)
        return res                