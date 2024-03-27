class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        curr = []
        nums.sort()

        def dfs(curr, idx):
            res.append(curr.copy())

            for i in range(idx, len(nums)):  # 每一次如果有多个相同元素，那么只有第一个元素进去
                if i != idx and nums[i - 1] == nums[i]: continue  # 比如原本是[], 那么这一层loop只会有[2]一次，后面不会产生同样的
                curr.append(nums[i])
                dfs(curr, i + 1)
                curr.pop()

            return

        dfs(curr, 0)

        return res

