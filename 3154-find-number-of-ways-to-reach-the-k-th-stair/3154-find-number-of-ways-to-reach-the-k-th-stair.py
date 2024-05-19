class Solution:
    def waysToReachStair(self, k: int) -> int:
        @cache
        def dfs(cur=1, jump=0, typ=2):
            if cur - k > 1:
                return 0
            res = 0
            if cur == k:
                res += 1
            if typ == 2 and cur != 0:
                res +=dfs(cur-1, jump, 1)
                
            res += dfs(cur + 2**jump, jump+1, 2)
            return res
        return dfs()