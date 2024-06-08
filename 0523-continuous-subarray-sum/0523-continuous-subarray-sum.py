class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        l, m = 0, -1
        s = set()
        for n in nums:
            t, l = l, (l+n) % k
            if l in s:
                return True
            m = t
            s.add(m)
        return False