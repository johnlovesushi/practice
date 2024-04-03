class Solution:
    def trap(self, height: List[int]) -> int:

        # method 1: monotonic stack

        # stack = []
        # res = 0

        # for i in range(len(height)):
        #     # 单调递减才不会存储水
        #     while stack and height[i] > height[stack[-1]]:
        #         prev = stack.pop()
        #         if not stack: break # 如果pop 完之后stack为空了
        #         res+= (min(height[i],height[stack[-1]]) - height[prev])*(i - stack[-1] - 1) if min(height[i],height[stack[-1]]) > height[prev] else 0
        #     stack.append(i)

        # return res

        # method 2: dp
        N = len(height)
        left, right = [0] * N, [0] * N
        res = 0
        left[0] = height[0]
        right[-1] = height[-1]
        for i in range(1, N):
            left[i] = max(left[i - 1], height[i])

        for j in range(N - 2, -1, -1):
            right[j] = max(right[j + 1], height[j])

        for i in range(N):
            res += min(left[i], right[i]) - height[i]

        return res