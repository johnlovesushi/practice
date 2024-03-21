class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        res = []
        visited = {}  # {nums[i]: i}

        for i in range(len(nums)):
            reminder = target - nums[i]
            if reminder in visited:
                return [visited[reminder], i]
            else:
                visited[nums[i]] = i

        return 