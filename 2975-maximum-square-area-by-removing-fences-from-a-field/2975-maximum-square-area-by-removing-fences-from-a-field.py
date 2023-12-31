class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.sort()
        vFences.sort()
        ch = [1]
        hs = set()
        hFences.append(m)
        for h in hFences:
            for i in ch:
                hs.add(h-i)
            ch.append(h)
        cv = [1]
        vs = set()
        vFences.append(n)
        for v in vFences:
            for i in cv:
                vs.add(v-i)
            cv.append(v)
        # print(hs,vs)
        t = hs & vs
        if t:
            return max(t)**2 % (10**9+7)
        else:
            return -1