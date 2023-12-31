class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        s = set(range(1,(len(grid)**2)+1))
        # print(s)
        res = 0
        
        for g in grid:
            for i in g:
                if i not in s:
                    res = i
                s -= {i}
                    
        # print(s)
        for i in s:
            return res,i