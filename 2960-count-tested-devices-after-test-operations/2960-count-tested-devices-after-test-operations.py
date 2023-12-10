class Solution:
    def countTestedDevices(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                res += 1
                nums[i+1:] = list(map(lambda x:x-1,nums[i+1:]))
        return res