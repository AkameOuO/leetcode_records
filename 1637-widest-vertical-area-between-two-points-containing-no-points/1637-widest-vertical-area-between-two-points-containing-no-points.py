class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted(map(lambda x:x[0],points))
        res = 0
        for i in range(1,len(points)):
            res = max(res,points[i]-points[i-1])
        return res