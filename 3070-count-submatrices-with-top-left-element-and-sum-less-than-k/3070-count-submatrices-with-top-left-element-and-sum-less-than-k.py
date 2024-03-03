class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        res = 0
        m = [[g[0]] for g in grid]
        for rg,rm in zip(grid,m):
            for n in rg[1:]:
                rm.append(rm[-1]+n)
        for i in range(len(grid)-1):
            for j in range(len(grid[0])):
                m[i+1][j] += m[i][j]
        for r in m:
            for n in r:
                if n <= k:
                    res += 1
        return res