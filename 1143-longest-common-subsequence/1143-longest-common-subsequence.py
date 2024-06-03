class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        @cache
        def dp(a,b):
            if a == len(s) or b == len(t):
                return 0
            if s[a] == t[b]:
                return dp(a+1, b+1) + 1
            
            return max(dp(a+1, b), dp(a, b+1)) 
        return dp(0,0)