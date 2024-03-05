class Solution:
    def minimumLength(self, s: str) -> int:
        while s:
            if s[0] != s[-1] or len(s) == 1:
                break
            t = s[0]
            i, j = 0, len(s) - 1
            while i <= j and s[i] == t:
                i += 1
            while j >= i and s[j] == t:
                j -= 1
            s = s[i:j+1]
        return len(s)