class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = list(map(lambda x:~x+2,nums))
        heapify(nums)
        return heappop(nums) * heappop(nums)