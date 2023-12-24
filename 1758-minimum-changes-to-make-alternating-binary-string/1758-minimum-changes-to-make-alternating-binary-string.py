class Solution:
    def minOperations(self, s: str) -> int:
        res = 0
        last = s[0]
        for i in range(1,len(s)):
            # print(s[i],last)
            res += (s[i] == last)
            last = ("0" if last == "1" else "1")
        return min(res,len(s)-res)