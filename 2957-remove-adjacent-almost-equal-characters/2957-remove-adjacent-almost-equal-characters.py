class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        last = 0
        res = 0
        for ch in word:
            if abs(ord(ch)-last) < 2:
                res += 1
                last = 0
            else:
                last = ord(ch)
        return res