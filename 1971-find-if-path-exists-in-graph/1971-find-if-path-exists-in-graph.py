class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = {source}
        m = defaultdict(set)
        for f,t in edges:
            m[f].add(t)
            m[t].add(f)
        l = [source]
        for i in l:
            if i == destination:
                return True
            for j in m[i]:
                if j not in visited:
                    visited.add(j)
                    l.append(j)
        return False