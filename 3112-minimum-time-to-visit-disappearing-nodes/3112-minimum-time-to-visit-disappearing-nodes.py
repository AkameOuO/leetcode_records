class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        m = defaultdict(lambda :defaultdict(lambda :10**6))
        for a,b,l in edges:
            m[a][b] = min(m[a][b], l)
            m[b][a] = m[a][b]
        res = [10**9] * n
        heap = [(0,0)]
        while heap:
            time, cur= heappop(heap)
            if time >= disappear[cur] or time >= res[cur]:
                continue
            res[cur] = time
            for k,v in m[cur].items():
                if time+v >= disappear[k]\
                or time+v >= res[k]:
                    continue
                heappush(heap,(time+v,k))
        
        return [i if i < 10**9 else -1 for i in res]
            