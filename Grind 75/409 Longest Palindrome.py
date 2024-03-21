class Solution:
    def longestPalindrome(self, s: str) -> int:

        # 解法： 其实所有的偶数都可以直接相加，但是只有要奇数存在的话，每一个奇数都要去掉1， 所有就是所有数值相加，然后计量有多少奇数，然后只要这个
        # 奇数的数值不为0，那么就需要减掉然后+1， 如果没有奇数，那么就直接return
        count = Counter(s)
        res = 0
        odd = 0
        for val in count.values():
            if val % 2 == 0:
                res += val
            else:
                res += val
                odd += 1

        return res - odd + 1 if odd else res