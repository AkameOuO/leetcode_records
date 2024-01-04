class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = Counter(nums)
        t = 0
        for v in c.values():
            if v == 1:
                return -1
            if v % 3 == 1:
                v += 2
            elif v % 3 == 2:
                v += 1
            t += v // 3
        return t