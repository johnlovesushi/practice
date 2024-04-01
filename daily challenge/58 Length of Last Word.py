class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # strip 去掉多余的空格，然后split()以空格区分
        return len(s.strip().split(" ")[-1])