class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        s = tickets[k]
        r = 0
        for i, t in zip(count(),tickets):
            if i <= k:
                r += min(s,t)
            else:
                r += min(s-1,t)
        return r
            