from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # brute force : 暴力解法
        # TimeComplexity O(n^2) 超时
        # res = []

        # for i in range(len(nums)-k+1):
        #     res.append(max(nums[i:i+k]))
        # return res

        # method 2: priority queue

        res = []
        queue = deque()

        for i in range(len(nums)):
            while queue and queue[0] + k <= i:
                queue.popleft()
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            queue.append(i)
            # print(queue)
            if i >= k - 1:
                res.append(nums[queue[0]])

        return res
