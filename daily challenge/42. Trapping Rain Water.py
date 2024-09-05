class Solution:
    def trap(self, height: List[int]) -> int:

        # method 1: dp
        l,r = 0, len(height)-1

        leftMax, rightMax= [0]*len(height),[0]*len(height)
        leftMax[0] = height[0]
        rightMax[-1] = height[-1]

        for i in range(1,len(height)):
            leftMax[i] = max(leftMax[i-1],height[i])

        for j in range(len(height)-2,-1,-1):
            rightMax[j] = max(rightMax[j+1], height[j])

        res = 0
        # print(leftMax)
        # print(rightMax)
        for i in range(1,len(height)-1):
            res+= max(min(leftMax[i],rightMax[i])-height[i],0)

        return res

        # method 2: monotonic stack
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:  # 如果小于height[i]
                prev = stack.pop()
                if not stack: break
                res += (min(height[i], height[stack[-1]]) - height[prev]) * (i - stack[-1] - 1) if min(height[i],
                                                                                                       height[
                                                                                                           stack[-1]]) > \
                                                                                                   height[prev] else 0
            stack.append(i)

        return res

