class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        l, m = 0, 0
        s = set()
        for n in nums:
            if (l+n) % k in s:
                return True
            m, l = l, (l+n) % k
            s.add(m)
        return False