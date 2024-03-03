from bisect import *

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        a1 = []
        a2 = []
        b1 = []
        b2 = []
        for n in nums:
            if not a1:
                a1.append(n)
                b1.append(n)
                continue
            if not a2:
                a2.append(n)
                b2.append(n)
                continue
            
            i1 = len(b1) - bisect(b1,n)
            i2 = len(b2) - bisect(b2,n)
            if i1 > i2:
                a1.append(n)
                insort(b1,n)
            elif i1 < i2:
                a2.append(n)
                insort(b2,n)
            else:
                if len(a2) < len(a1):
                    a2.append(n)
                    insort(b2,n)
                else:
                    a1.append(n)
                    insort(b1,n)
        return a1+a2
            