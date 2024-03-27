class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        # [1,1,2]
        visited = [False] * len(nums)
        curr = []
        res = []
        nums.sort()  # 如果有两个相同元素，必须sort，这样才能知道相同元素的位置关系

        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                # 确保不会使用重复元素, 后半边和subset II 是一样的，比如[]的情况，我们加了第一个1，但不想加入第二个1 变成[1]的情况;
                if visited[i] or (i > 0 and nums[i - 1] == nums[i] and not visited[i - 1]): continue
                curr.append(nums[i])
                visited[i] = True
                dfs(curr)
                visited[i] = False
                curr.pop()
            return

        dfs(curr)
        return res