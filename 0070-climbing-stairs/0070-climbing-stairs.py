class Solution:
    def climbStairs(self, n: int) -> int:
        l = [1,1]
        for _ in range(n-1):
            l.append(l[-1]+l[-2])
        return l[n]