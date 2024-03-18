class Solution:
    def isValid(self, s: str) -> bool:

        stk = []
        dict = {")": "(", "]": "[", "}": "{"}
        for i in range(len(s)):
            if not stk and s[i] in dict:
                return False

            if s[i] in dict:
                if stk[-1] != dict[s[i]]:
                    return False
                else:
                    stk.pop()
            else:
                stk.append(s[i])

        return not stk