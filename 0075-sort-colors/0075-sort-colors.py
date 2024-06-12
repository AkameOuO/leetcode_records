class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = Counter(nums)
        for i in range(len(nums)):
            if i < c[0]:
                nums[i] = 0
            elif c[0] <= i < c[0] + c[1]:
                nums[i] = 1
            else:
                nums[i] = 2