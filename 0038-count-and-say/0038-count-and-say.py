@cache
def solve(n):
    if n == 1:
        return "1"
    s = solve(n-1)
    last = ""
    cur = ""
    res = ""
    for c in s:
        if c == last:
            cur += 1
        else:
            res += str(cur) + last
            cur = 1
            last = c
    res += str(cur) + last
    return res
            
        
class Solution:
    def countAndSay(self, n: int) -> str:
        return solve(n)