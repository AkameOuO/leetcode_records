class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        tot = set()
        c = Counter()
        for w,l in matches:
            tot |= {w,l}
            c[l] += 1
        res = [[],[]]
        for p in sorted(tot):
            if c[p] < 2:
                res[c[p]].append(p)
        return res