class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = Counter(magazine)

        for c in ransomNote:
            magazine[c] = magazine.get(c, 0) - 1
            if magazine[c] < 0:
                return False

        return True