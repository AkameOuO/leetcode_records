class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        index = 0;
        def iden():
            nonlocal index
            index += 1
            return index - 1
        res = [False] * len(edges)
        rec = [math.inf] * n
        m = defaultdict(lambda:defaultdict(tuple))
        for i,(f,t,w) in zip(count(),edges):
            m[f][t] = w,i
            m[t][f] = w,i
        heap = []
        mincost = math.inf
        heappush(heap,(0,0,iden(),[]))
        while heap:
            cost, node, _, path = heappop(heap)
            if cost > mincost:
                break
            if node == n - 1:
                mincost = cost
                for p in path:
                    res[p] = True
            rec[node] = min(rec[node],cost)
            for k,(v,i) in m[node].items():
                if rec[k] < cost+v:
                    continue
                heappush(heap,(cost+v,k,iden(),path+[i]))
        return res
            
            
            
            