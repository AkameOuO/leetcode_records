class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        
        for i,n in zip(count(),nums):
            d[n].append(i)
        
        t = [u[1] for u in sorted(d.items())]
        # print(t)
        m,n = 0,0
        
        s = sum(nums)
        res = []
        for i,k in queries:
            if m >= len(t):
                res.append(0)
                continue
            s -= nums[i]
            nums[i] = 0
            x = 0
            while k and m < len(t):
                while k and n < len(t[m]):
                    if nums[t[m][n]]:
                        s -= nums[t[m][n]]
                        nums[t[m][n]] = 0
                        k -= 1
                    n += 1
                if k:
                    n = 0
                    m += 1
                # print(m,n)
            res.append(s)
        return res