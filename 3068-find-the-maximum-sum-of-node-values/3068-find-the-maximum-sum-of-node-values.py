class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        nums.sort(key=lambda x: x - (x^k))
        res = sum(nums)
        for i in range(1,len(nums),2):
            j = i-1
            if (t:=((nums[i]^k)-nums[i] + (nums[j]^k)-nums[j])) > 0:
                res += t
            else:
                break
        return res