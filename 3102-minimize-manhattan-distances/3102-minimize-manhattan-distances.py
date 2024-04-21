class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        l1, l2 = [], []
        for i,(x,y) in zip(count(),points):
            l1.append((x+y,i))
            l2.append((x-y,i))
        # print(l1,l2)
        l1.sort()
        l2.sort()
        # print(l1,l2)
        res = float("inf")
        for i in range(len(points)):
            l = []
            for k in range(3):
                if l1[k][1] == i:
                    continue
                if len(l) == 2:
                    break
                l.append(l1[k][0])
            for k in range(-1,-4,-1):
                if l1[k][1] == i:
                    continue
                if len(l) == 4:
                    break
                l.append(l1[k][0])
            t = [
                l[-1] - l[1],
                l[-2] - l[0],
                l[-1] - l[0],
            ]
            l = []
            for k in range(3):
                if l2[k][1] == i:
                    continue
                if len(l) == 2:
                    break
                l.append(l2[k][0])
            for k in range(-1,-4,-1):
                if l2[k][1] == i:
                    continue
                if len(l) == 4:
                    break
                l.append(l2[k][0])
            t += [
                l[-1] - l[1],
                l[-2] - l[0],
                l[-1] - l[0],
            ]
            res = min(res,max(t))
        return res