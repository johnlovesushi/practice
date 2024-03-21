# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        # 解法在于：
        # T T T F F
        # m = 3的时候，说明第一个false在右边不包括当前，所以l = m + 1
        # m = 4的时候，说明第一个false在左边，但是包括当前，所以r = m
        # 最后结束的结果一定是，l = r, 所以while l < r
        l, r = 1, n
        while l < r:
            m = l + (r - l) // 2
            print(m)
            if isBadVersion(m):  # True
                r = m
            else:
                l = m + 1

        return l