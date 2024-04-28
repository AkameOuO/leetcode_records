class Solution:
    def minEnd(self, n: int, x: int) -> int:
        if n == 1:
            return x
        res = 0
        i = 0
        n -= 1
        while n or x:
            if x&1:
                res |= 1 << i
            else:
                res |= (n&1) << i
                n >>= 1
            x >>= 1
            i += 1
        return res