class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False]*(len(s) + 1)
        dp[-1] = True

        for idx in range(len(dp)-1,-1,-1):
            for word in wordDict:
                print(idx, word)
                if s[idx - len(word):idx] == word:
                    if dp[idx]:
                        dp[idx - len(word)] = dp[idx]
        #print(dp)
        return dp[0]