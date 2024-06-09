class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        l = 0
        c = Counter([0])
        r = 0
        for n in nums:
            l = (l+n) % k
            r += c[l]
            c[l] += 1
            
        return r