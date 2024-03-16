class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans=0
        d={0:-1}
        nums=list(accumulate(map(lambda x:1 if x else -1,nums)))
        for i in range(len(nums)):
            if nums[i] in d:
                ans=max(ans,i-d[nums[i]])
            else:
                d[nums[i]]=i
        return ans
        