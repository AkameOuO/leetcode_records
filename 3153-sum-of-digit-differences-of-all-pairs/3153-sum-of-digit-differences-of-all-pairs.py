class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        k = len(str(nums[0]))
        cs = map(Counter,zip(*map(str,nums)))
        res = 0
        for c in cs:
            l = len(nums)
            for v in c.values():
                res += v * (l-v)
                l -= v
        return res