class Solution:
    def pivotInteger(self, n: int) -> int:
        return int(s**0.5) if int((s:=(n * (n+1) // 2))**0.5)**2 == s else -1