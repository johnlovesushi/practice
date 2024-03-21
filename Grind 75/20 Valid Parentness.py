class Solution:
    def isValid(self, s: str) -> bool:

        map = {"]": "[", ")": "(", "}": "{"}

        stk = []

        for c in s:
            if c in map:
                if stk and stk[-1] == map[c]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)

        return not stk
