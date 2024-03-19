class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        l = sorted(Counter(tasks).values(),reverse=True)
        t = l[0]
        res = 1 + (t-1) * (n+1)
        for n in l[1:]:
            if n == t:
                res += 1
        res = max(res,sum(l))
        return res