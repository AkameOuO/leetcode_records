class Solution:
    def isPathCrossing(self, path: str) -> bool:
        d = {
            "N":(0,1),
            "S":(0,-1),
            "E":(1,0),
            "W":(-1,0)
        }
        x,y = 0,0
        s = {(x,y)}
        for c in path:
            a,b = d[c]
            x+=a
            y+=b
            if (x,y) in s:
                return True
            s.add((x,y))
        return False