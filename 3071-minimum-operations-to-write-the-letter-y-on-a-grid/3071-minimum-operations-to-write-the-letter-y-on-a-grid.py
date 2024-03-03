class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        yc = Counter()
        nyc = Counter()
        for r in grid:
            nyc += Counter(r)
        yc[3] = 0
        yc[grid[len(grid)//2][len(grid)//2]] += 1
        for i in range(len(grid)//2):
            yc[grid[i][i]] += 1
            yc[grid[i][-i-1]] += 1
            yc[grid[-i-1][len(grid)//2]] += 1
        
        nyc -= yc
        # print(yc,nyc)
        res = 999999
        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                res = min(res,len(grid)**2 - nyc[i] - yc[j])
            
        return res