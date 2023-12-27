class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        for c,t in zip(colors,neededTime):
            try:
                if c == lc:
                    if t < lt:
                        res += t
                        continue
                    else:
                        res += lt
                lc,lt = c,t
            except NameError:
                lc,lt = c,t
        return res