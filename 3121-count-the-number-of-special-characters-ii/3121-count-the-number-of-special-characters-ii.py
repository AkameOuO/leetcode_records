class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        res = 0
        for ch in ascii_lowercase:
            chu = ch.upper()
            a,b = word.find(chu), word.rfind(ch)
            if a >= 0 and b >= 0 and a > b:
                res += 1
        return res