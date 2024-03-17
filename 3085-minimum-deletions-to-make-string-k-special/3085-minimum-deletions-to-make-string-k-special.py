class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        c = Counter(word)
        v = sorted(c.values())
        res = 10**9
        cur = 0
        for i in range(len(v)):
            x,y = sum(map(lambda x:max(x-k-v[i],0),v)), sum(v[:i])
            res = min(res,x+y)
        return res
        