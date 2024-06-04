class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        r = sum(map(lambda x:(x|1)^1, c.values()))
        if any(map(lambda x:x%2 == 1, c.values())):
            r += 1
        return r