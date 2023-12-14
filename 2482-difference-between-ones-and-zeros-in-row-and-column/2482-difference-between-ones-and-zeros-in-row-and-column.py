class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        return (cs:=[sum(col)*2-len(grid) for col in zip(*grid)],[[c+r for c in cs] for r in [sum(row)*2-len(grid[0]) for row in grid]])[1]