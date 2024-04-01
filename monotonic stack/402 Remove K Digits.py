class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        if len(num) == k: return "0"
        stack = []
        count = 0

        for i in range(len(num)):
            while stack and stack[-1] > num[i] and count < k:
                stack.pop()
                count += 1
            stack.append(num[i])

        while count < k:
            stack.pop()
            count += 1

        while len(stack) >= 2 and stack[0] == "0": stack.remove("0")
        return ("").join(stack)