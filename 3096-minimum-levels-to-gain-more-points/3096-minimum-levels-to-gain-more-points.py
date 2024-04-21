class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        c = Counter(possible)
        t = c[1] - c[0]
        m, n = 0, t
        for i, p in zip(count(),possible[:-1]):
            if p:
                m += 1
                n -= 1
            else:
                m -= 1
                n += 1
            if m > n:
                return i + 1
        return -1
            
                