class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:

        # res = float("infinity")
        # queue = deque()
        # # return the length of shorest non-empty subarray
        # for i in range(len(nums)):
        #     queue.append(nums[i])
        #     while queue and sum(queue) >= k:
        #         res = min(res, len(queue))
        #         queue.popleft()

        #     print(queue)
        # #if sum(queue) >= k: res = min(res, len(queue))

        # return -1 if res == float("infinity") else res

        # 使用递增的queue
        n = len(nums)
        prefixSum = [0] * (n + 1)
        for i in range(1, len(prefixSum)):
            prefixSum[i] = prefixSum[i - 1] + nums[i - 1]

        # print(prefixSum)
        queue = deque()
        res = float("infinity")
        for i in range(len(prefixSum)):
            while queue and prefixSum[i] - prefixSum[queue[0]] >= k:
                res = min(res, i - queue.popleft())

            while queue and prefixSum[i] < prefixSum[queue[-1]]:
                queue.pop()

            queue.append(i)
            # print(queue,i)
        return res if res != float("infinity") else -1

