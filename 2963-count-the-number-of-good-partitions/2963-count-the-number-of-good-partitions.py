class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        d = {}
        for i,n in enumerate(nums):
            if n in d:
                d[n] = (d[n][0],i)
            else:
                d[n] = (i,i)
        l = sorted(d.values())
        res = 0
        cur = -1
        for a,b in l:
            if a < cur:
                cur = max(cur,b)
            else:
                cur = b
                res += 1
        return pow(2,res-1,10**9+7)