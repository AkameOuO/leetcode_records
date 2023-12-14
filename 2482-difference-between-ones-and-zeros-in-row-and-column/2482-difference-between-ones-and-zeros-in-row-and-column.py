class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        rs = [sum(row)*2-n for row in grid]
        cs = [sum(col)*2-m for col in zip(*grid)]
        res = []
        for r in rs:
            res.append([])
            for c in cs:
                res[-1].append(r+c)
        return res