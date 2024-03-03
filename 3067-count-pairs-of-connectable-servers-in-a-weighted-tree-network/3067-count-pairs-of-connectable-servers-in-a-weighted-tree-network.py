class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        d = defaultdict(dict)
        ans = []
        for x,y,c in edges:
            d[x][y] = c
            d[y][x] = c
            
        def dfs(last,cur,cost):
            nonlocal signalSpeed
            res = 1 if cost % signalSpeed == 0 else 0
            for n,m in d[cur].items():
                if n == last:
                    continue
                res += dfs(cur,n,cost+m)
            return res
        
        for i in range(len(edges)+1):
            l = []
            t = 0
            for n,m in d[i].items():
                l.append(dfs(i,n,m))
            for j in range(len(l)-1):
                for k in range(j+1,len(l)):
                    t += l[j]*l[k]
            ans.append(t)
        return ans