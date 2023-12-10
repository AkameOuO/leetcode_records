class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        t = max(nums)
        l = list(filter(lambda x:nums[x] == t,range(len(nums))))
        if len(l) < k:
            return 0
        res = 0
        last = -1
        for i in range(len(l)-k+1):
            # s = l[i:i+k]
            res += (l[i] - last) * (len(nums) - l[i+k-1])
            last = l[i]
            # print(s,l[i] - last,len(nums) - l[i+k-1],res)
        print(l)
        return res