class Solution:
    def clearDigits(self, s: str) -> str:
        l = []
        for c in s:
            if c in "0123456789":
                l.pop()
            else:
                l.append(c)
        return "".join(l)