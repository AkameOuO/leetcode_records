class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        res = 0
        while len(nums) > 1:
            x,y = heappop(nums), heappop(nums)
            if x >= k:
                return res
            heappush(nums,x*2+y)
            res += 1
        return res