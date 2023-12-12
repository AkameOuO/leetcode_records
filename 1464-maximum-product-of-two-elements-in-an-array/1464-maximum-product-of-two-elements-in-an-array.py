class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return (heapify(nums:=list(map(lambda x:~x+2,nums))),heappop(nums) * heappop(nums))[1]