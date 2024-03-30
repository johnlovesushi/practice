# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        l, r = 1, n

        # while l < r:
        #     m = l + (r - l) // 2
        #     if isBadVersion(m):  # 说明是bad, 那么我们要前移，但是有可能就是第一个bad
        #         r = m
        #     else:  # 说明不是bad，需要右移，但是mid 当前是false, 所以l = m+1
        #         l = m + 1
        #
        # return r  # 最后停止条件是l == r, 所以while 是 l<r