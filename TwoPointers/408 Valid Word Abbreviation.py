class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0

        while i < len(word) and j < len(abbr):
            print(i, j)
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j] <= '0' or abbr[j] > '9':
                return False
            else:
                start = j
                num = 0
                while j < len(abbr) and abbr[j] >= '0' and abbr[j] <= '9':
                    num = num * 10 + int(abbr[j])
                    j += 1
                i += num

        return i == len(word) and j == len(abbr)

