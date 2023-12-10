class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        c = Counter()
        res = 0
        left = 0
        for i,n in enumerate(nums):
            c[n] += 1
            if c[n] > k:
                while nums[left] != n:
                    c[nums[left]] -= 1
                    left += 1
                c[nums[left]] -= 1
                left += 1
            res = max(res,i-left+1)
        return res
                    
                