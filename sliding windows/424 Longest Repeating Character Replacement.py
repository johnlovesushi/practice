class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        have = dict()
        l = 0
        res = 0
        for r in range(len(s)):
            have[s[r]] = 1 + have.get(s[r], 0)

            max_element = max(have.values())

            while r - l + 1 - max_element > k:
                have[s[l]] -= 1
                max_element = max(have.values())
                l += 1
            res = max(res, r - l + 1)

        return res
