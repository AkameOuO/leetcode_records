class Solution:
    def maxScore(self, s: str) -> int:
        res = Counter(s[1:])["1"] + 1 - int(s[0])
        cur = res
        for c in s[1:-1]:
            cur += -1 if int(c) else 1
            res = max(res,cur)
        return res
        