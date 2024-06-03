class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        try:
            i = iter(t)
            n = next(i)
            r = len(t)
            for c in s:
                if n == c:
                    n = next(i)
                    r -= 1
            return r
        except:
            return 0