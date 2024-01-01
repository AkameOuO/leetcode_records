class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort(reverse=True)
        g.sort(reverse=True)
        r = 0
        while s and g:
            a,b = g.pop(),s.pop()
            
            while s and b < a:
                b = s.pop()
            r += b >= a
        return r
        