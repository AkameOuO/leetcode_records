class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        t = s[::-1]
        for i in range(len(s)-1):
            if s[i:i+2] in t:
                return True
        return False