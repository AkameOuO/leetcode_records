class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        l = sorted(map(lambda x:x[0],points))
        last = - w - 1
        res = 0
        for x in l:
            if x - last > w:
                res += 1
                last = x
        return res