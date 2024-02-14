class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a = filter(lambda x:x>0,nums)
        b = filter(lambda x:x<0,nums)
        res = []
        for z in zip(a,b):
            res.extend(z)
        return res
            