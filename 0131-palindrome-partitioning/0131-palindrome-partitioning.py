class Solution:
    def __init__(self):
        self.isPalin = lambda x:x == x[::-1]
        self.res = list()
        
    def partition(self, s: str,path = list()) -> List[List[str]]:
        if not s:
            self.res.append(path)
            
            
            
        for i in range(1, len(s)+1):
            if self.isPalin(s[:i]):
                
                # path.append(s[:i])
                self.partition(s[i:], path + [s[:i]])
        return self.res
                
   
            