class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        heapify(nums)
        while nums:
            a,b = heappop(nums),heappop(nums)
            arr += [b,a]
        return arr
        