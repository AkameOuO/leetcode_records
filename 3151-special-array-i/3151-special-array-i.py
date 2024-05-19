class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        last = nums[0]
        for n in nums[1:]:
            if not (1 & (last^n)):
                return False
            last = n
            
        return True