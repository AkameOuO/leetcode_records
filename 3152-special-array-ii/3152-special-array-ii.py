class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        m = [0]
        
        last = nums[0]
        for i in range(1,len(nums)):
            n = nums[i]
            if not (1 & (last^n)):
                m.append(i)
            else:
                m.append(m[-1])
            last = n
        res = []
        for f,t in queries:
            res.append(m[t] <= f)
        return res