class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if max(Counter(s[i:j+1]).values()) < 3:
                    res = max(res,j-i+1)
        return res