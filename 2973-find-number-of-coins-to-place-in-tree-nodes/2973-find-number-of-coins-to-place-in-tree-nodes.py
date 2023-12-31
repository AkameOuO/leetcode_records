class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        ne = defaultdict(set)
        res = [0] * len(cost)
        for n1,n2 in edges:
            ne[n1].add(n2)
            ne[n2].add(n1)
        def dfs(cur,last=-1):
            try:
                ne[cur].remove(last)
            except:
                pass
            t = [cost[cur]]
            # if len(ne[cur]) == 0:
            #     return t
            for n in ne[cur]:
                t += dfs(n,cur)
                t.sort()
                if len(t) > 5:
                    t = t[:3] + t[-3:]
            if len(t) < 3:
                res[cur] = 1
            else:
                res[cur] = max(0,t[0]*t[1]*t[-1],t[-1]*t[-2]*t[-3])
            return t
        dfs(0)
        return res
        # print(tree)
        # return [1 if len(tree[i]) < 3 else max(0,(t:=sorted(map(lambda x:cost[x],tree[i])))[0]*t[1]*t[-1],t[-1]*t[-2]*t[-3]) for i in range(len(cost))]