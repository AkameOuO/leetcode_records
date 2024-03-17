class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        flag = True
        for i in intervals:
            if i[1] < newInterval[0] or newInterval[1] < i[0]:
                res.append(i)
                continue
            if newInterval[0] <= i[1]:
                newInterval[0] = min(newInterval[0],i[0])
                if flag:
                    res.append(newInterval)
                    flag = False
                        
            if newInterval[1] >= i[0]:
                newInterval[1] = max(newInterval[1],i[1])
        
        if flag:
            res.append(newInterval)
            res.sort(key=tuple)
        return res
            
            