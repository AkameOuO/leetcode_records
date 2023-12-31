class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        for i in range(len(s)-1,-1,-1):
            res = max(res,i-s.index(s[i])-1)
        return res