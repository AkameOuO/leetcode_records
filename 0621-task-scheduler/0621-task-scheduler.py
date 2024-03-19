class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        l = sorted(Counter(tasks).values(),reverse=True)
        t = l[0]
        res = (t-1) * (n+1)
        for n in l:
            if n == t:
                res += 1
        return max(res,sum(l))