class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        # k = 2
        # visited = set()
        # freq = dict()
        # l = 0
        # res = 0
        # for r in range(len(s)):
        #     # 先加入然后检查什么时候复合条件
        #     freq[s[r]] = 1 + freq.get(s[r],0)
        #     if s[r] not in visited:
        #         visited.add(s[r])

        #     while len(visited) > k:
        #         freq[s[l]]-=1
        #         if freq[s[l]] == 0:
        #             visited.remove(s[l])
        #         l+=1

        #     # 更新结果
        #     res = max(res, r-l+1)
        # return res

        # Update: 可以直接使用一个dict，然后如果freq变成了0，那么直接delete掉这个element就可以
        k = 2
        freq = dict()
        l = 0
        res = 0
        for r in range(len(s)):
            # 先加入然后检查什么时候复合条件
            freq[s[r]] = 1 + freq.get(s[r], 0)

            while len(freq) > k:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1

            # 更新结果
            res = max(res, r - l + 1)
        return res