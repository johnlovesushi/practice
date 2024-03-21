import collections

import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # method 1:
        if len(s) != len(t): return False
        ls = [0]*26
        lt = [0]*26

        for i in range(len(s)):
            ls[ord(s[i]) - ord('a')]+=1
            lt[ord(t[i]) - ord('a')]+=1

        return ls==lt

        # method 2:
        return Counter(s) == Counter(t)


