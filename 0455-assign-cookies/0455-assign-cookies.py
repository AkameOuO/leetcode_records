class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        heapify(s)
        heapify(g)
        r = 0
        while s and g:
            a,b = heappop(g),heappop(s)
            
            while s and b < a:
                b = heappop(s)
            r += b >= a
        return r
        