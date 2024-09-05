class Solution:
    def validPalindrome(self, s: str) -> bool:
        k = 0
        l, r = 0, len(s) - 1

        while l <= r and s[l] == s[r]:  # 修改了=条件，避免 abba这种
            l += 1
            r -= 1
        if l >= r: return True  # 同时说明都检查完了结束了上面的循环
        if s[l] != s[r]:
            if self.isPalindrome(s, l + 1, r) or self.isPalindrome(s, l, r - 1): return True

        return False

    def isPalindrome(self, s, l, r):

        while l <= r:
            if s[l] != s[r]: return False
            l += 1
            r -= 1
        return True