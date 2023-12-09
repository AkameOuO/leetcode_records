class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        m = defaultdict(lambda:100000)
        for a,b,c in roads:
            m[a,b] = min(m[a,b],c)
            m[b,a] = m[a,b]
        
        def dfs(s,t,disable,cur_cost,visited):
            if s == t:
                return cur_cost <= maxDistance
            for i in range(n):
                if i in disable or i in visited:
                    continue
                if (s,i) in m:
                    if dfs(i,t,disable,cur_cost+m[s,i],visited+[s]):
                        return True
            return False
                    
            
        def check(disable):
            for i in range(n):
                if i in disable:
                    continue
                for j in range(i+1,n):
                    if j in disable:
                        continue
                    if not dfs(i,j,disable,0,[]):
                        return False
            return True
        
        l = list(range(n-1,-1,-1))
        res = 0
        while l:
            res += check(l)
            p = l.pop()
            l.extend(range(p-1,-1,-1))
        return res+check([])