class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        def _maxl():
            nonlocal nums
            res = 0
            cur = 0
            for n in nums:
                if n:
                    cur += 1
                    res = max(res,cur)
                else:
                    cur = 0
            return res
        
        def find(n):
            nonlocal nums
            l = [] #deque()
            for i in range(len(nums)):
                if len(l) >= n:
                    break
                if nums[i]:
                    l.append(i)
            res = sum(map(lambda x:abs(x-l[(len(l)-1)//2]),l))
            cur = res
            for i in range(i,len(nums)):
                if nums[i]:
                    m = (len(l)-1)//2
                    cur -= abs(l[0]-l[m])
                    if len(l) % 2 == 0:
                        cur -= l[m+1] - l[m]
                    cur += abs(l[m+1]-i)
                    res= min(res,cur)
                    l.pop(0)
                    l.append(i)
            return res
        
        maxl = _maxl()
        
        if k - maxChanges - min(maxl,3) < 1:
            return k + max(0,k-min(maxl,3)) - (1 if maxl else 0)
        
        nums.append(0)
        k -= maxChanges
        return find(k) + maxChanges*2
        
            