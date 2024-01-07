class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [defaultdict(int) for _ in nums]
        res = 0
        for i,n in enumerate(nums):
            for j in range(i):
                m = nums[j]
                t = n-m
                dp[i][t] += 1
                res += dp[j][t]
                dp[i][t] += dp[j][t]
        return res
                