class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        lc = list(map(Counter,zip(*grid)))
        for c in lc:
            c[-1] = 0
        lc = list(map(lambda x:sorted(x.items(),key=lambda x:x[1],reverse=True),lc))
        @cache
        def dp(i, ln):
            nonlocal lc
            if i >= len(lc):
                return 0
            res = inf
            for ni,c in lc[i]:
                if ni != ln:
                    res = min(res,len(grid)-c+dp(i+1,ni))
            return res
        
        return dp(0,-1)
        