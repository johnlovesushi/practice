class Solution:
    def maxDepth(self, s: str) -> int:
        "2024-04-04"
        stack = []
        count = 0
        res = 0
        for c in s:
            if c == '(':
                stack.append(c)
                count+=1
                res = max(res,count)
            elif stack and c == ')':
                stack.pop()
                count-=1
        return res