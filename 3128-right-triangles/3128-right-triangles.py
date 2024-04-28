class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        l1 = list(map(sum,grid))
        l2 = list(map(sum,zip(*grid)))
        res = 0
        for i in range(len(l1)):
            for j in range(len(l2)):
                if grid[i][j]:
                    res += max(0,l1[i]-1) * max(0,l2[j]-1)
                # print(res)
        return res