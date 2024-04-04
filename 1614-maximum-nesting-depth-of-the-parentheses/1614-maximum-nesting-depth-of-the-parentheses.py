class Solution:
    def maxDepth(self, s: str) -> int:
        r,d = 0,0
        for c in s:
            if c == "(":
                r += 1
                d = max(r,d)
            elif c == ")":
                r -= 1
        return d