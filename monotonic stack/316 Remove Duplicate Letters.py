class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        "bcabc -> a:1, b:2, c:2 并且b先出现 所以结果是abc"
        # [b]
        # [b,c]
        # [a] -> b,c 因为发现后面还可以有b,c
        # [a,b]
        # [a,b,c]

        visited = set()
        stack = []
        last_idx = [-1] * 26
        for i in range(len(s)): last_idx[ord(s[i]) - ord('a')] = i
        for i in range(len(s)):
            c = s[i]  # 当前的char
            if c in visited: continue  # 如果已经被用过了 那么就不考虑了
            while stack and c < stack[-1] and i < last_idx[ord(stack[-1]) - ord('a')]:
                # 如果stack不是空，并且stack最上面的元素比c大并且我们发现stack最上面元素其实后面还可以有
                visited.remove(stack.pop())
            stack.append(c)
            visited.add(c)
            # print(stack)
        return "".join(stack)