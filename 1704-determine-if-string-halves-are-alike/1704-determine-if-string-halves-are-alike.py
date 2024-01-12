class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        res = 0
        for c in s[:len(s)//2]:
            res += (c in "aeiou")
        for c in s[len(s)//2:]:
            res -= (c in "aeiou")
        return res == 0