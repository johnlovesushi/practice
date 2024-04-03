class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        visited = set()
        res = 0
        for i in range(len(s)):
            while s[i] in visited:
                visited.remove(s[left])
                left += 1
            visited.add(s[i])

            res = max(res, i - left + 1)

        return res
