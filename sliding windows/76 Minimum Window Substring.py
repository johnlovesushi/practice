import Collection
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        curr = dict()
        have = 0
        l = 0
        res = [float("infinity"), 0, len(s) - 1]
        needed = Counter(t)
        need = len(needed)
        for r in range(len(s)):
            if s[r] in t:  # 说明原来没有
                needed[s[r]] -= 1
                if needed[s[r]] == 0:
                    have += 1

            # print(needed)
            # print(curr)
            while have >= need:
                if res[0] > r - l + 1:  # 满足条件 先更新结果
                    res[0] = r - l + 1
                    res[1] = l
                    res[2] = r

                if s[l] in needed:
                    needed[s[l]] += 1
                    if needed[s[l]] > 0:
                        have -= 1
                l += 1

        return "" if res[0] == float("infinity") else s[res[1]:res[2] + 1]

