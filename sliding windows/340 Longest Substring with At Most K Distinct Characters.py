class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        # 类似于159， 差别只是k可以是不只是2

        l = 0
        res = 0
        freq = {}
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            while len(freq) > k:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1

            res = max(res, r - l + 1)

        return res
