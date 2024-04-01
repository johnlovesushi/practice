class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # divide and conquer: 会超时
        # def calculateArea(heights, start, end):
        #     if start == end: return heights[start]
        #     if start > end: return 0
        #     minIndex = start
        #     for i in range(start,end+1):
        #         if heights[i] < heights[minIndex]: minIndex = i

        #     cur = heights[minIndex]*(end - start + 1)
        #     left = calculateArea(heights, start, minIndex - 1)
        #     right = calculateArea(heights,minIndex+1, end)
        #     return max(cur, left,right)

        # return calculateArea(heights, 0, len(heights) - 1)

        # monotonic stack

        stack = []
        res = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                prev = stack.pop()
                min_height = heights[prev]
                width = i - (0 if not stack else stack[-1] + 1)
                res = max(res, min_height * width)

            stack.append(i)

        while stack:
            prev = stack.pop()
            curr_height = heights[prev]
            width = len(heights) - (0 if not stack else stack[-1] + 1)
            res = max(res, width * curr_height)

        return res