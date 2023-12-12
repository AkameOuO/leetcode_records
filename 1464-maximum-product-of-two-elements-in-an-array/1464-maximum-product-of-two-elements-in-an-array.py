class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = list(map(lambda x:-x,nums))
        heapify(nums)
        return (heappop(nums)+1) * (heappop(nums)+1)