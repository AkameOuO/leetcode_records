class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        l = len(nums)
        @cache
        def dfs(i=0,cur=0,curl=0):
            nonlocal nums
            nonlocal l
            nonlocal k
            # nonlocal res
            if i >= l:
                return 0
            r = 0
            if cur + nums[i] < k:
                r = (r + dfs(i+1,cur+nums[i],curl+1)) % (10**9+7)
            elif cur + nums[i] == k:
                r = (r + 2 ** (l-curl-1)) % (10**9+7)
            
            r = (r + dfs(i+1,cur,curl)) % (10**9+7)
            return r
        
        return dfs()
            
                    