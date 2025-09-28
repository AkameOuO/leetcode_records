class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        while len(nums) >= 3:
            if nums[-2] + nums[-3] > nums[-1]:
                return sum(nums[-3:])
            nums.pop()
        return 0
