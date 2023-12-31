class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        def ispa(s):
            s = str(s)
            return s == s[::-1]
        def topa(num,num1):
            print(num,num1)
            for i in range(num,num1+1):
                if ispa(i):
                    return i,i
            res = [None,None]
            for i in count(1):
                if ispa(num-i):
                    if not res[0]:
                        res[0] = num-i
                    if res[1]:
                        return res
                if ispa(num1+i):
                    if not res[1]:
                        res[1] = num1+i
                    if res[0]:
                        return res
            
        nums.sort()
        if len(nums) %2 == 1:
            mid = [nums[len(nums)//2]]*2
        else:
            mid = [nums[len(nums)//2-1],nums[len(nums)//2]]
        r = topa(*mid)
        print(r)
        return min(sum(map(lambda x:abs(x-r[0]),nums)),sum(map(lambda x:abs(x-r[1]),nums)))