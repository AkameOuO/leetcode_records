class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if (l:=len(nums)) == sum(nums):
            return l-1
        cur,last,res = 0,0,0
        for n in nums:
            if n == 0:
                last,cur = cur,0
            else:
                cur += 1
            res = max(res,cur+last)
        return res