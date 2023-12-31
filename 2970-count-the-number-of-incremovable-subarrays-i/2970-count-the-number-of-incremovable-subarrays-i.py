class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        res = 0
        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                break
        else:
            return len(nums) * (1 + len(nums)) // 2
        i -= 1
        res = i+1
        tmp = 0
        # print(res)
        for j in range(1,len(nums)):
            while nums[-j] <= nums[i] and i > -1:
                i -= 1
            res += i+1+1
            # print(j,res)
            if nums[-j] <= nums[-j-1]:
                break
        return res+1
            
        # @cache
        # def dp(index):
        #     nonlocal nums
        #     count = 1
        #     for i in range(index,len(nums)):
        #         if nums[i] > nums[index]:
        #             count += dp(i)
        #     return count
        # return sum(map(dp,range(len(nums))))
            
        