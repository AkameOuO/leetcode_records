class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = [-1]
        m = 0
        for i,n in zip(count(), nums):
            if m < n:
                m = n
                l = [-1,i]
            elif m == n:
                l.append(i)
        if len(l) <= k:
            return 0
        res = 0
        for i in range(1,len(l) - k+1):
            res += (l[i] - l[i-1]) * (len(nums) - l[i+k-1])
            print(l[i],l[i] - l[i-1],len(nums) - l[i+k-1])
        return res