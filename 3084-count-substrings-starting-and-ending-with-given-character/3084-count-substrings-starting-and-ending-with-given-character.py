class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        t = Counter(s)[c]
        return t * (t+1) // 2