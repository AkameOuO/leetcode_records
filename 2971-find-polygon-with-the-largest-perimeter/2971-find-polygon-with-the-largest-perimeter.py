class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        res = s = sum(nums)
        for n in nums:
            s -= n
            if s <= n:
                res -= n
            else:
                return res
        return -1
            