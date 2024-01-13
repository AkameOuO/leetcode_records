class Solution:
    def minSteps(self, s: str, t: str) -> int:
        a = Counter(s)
        b = Counter(t)
        return sum([abs(a[c]-b[c]) for c in ascii_lowercase])//2