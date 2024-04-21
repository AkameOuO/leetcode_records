class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        stack = []
        res = 0
        for n in nums:
            while stack and stack[-1][0] < n:
                stack.pop()
            if not stack or n < stack[-1][0]:
                stack.append([n,1])
            elif n == stack[-1][0]:
                stack[-1][1] += 1
            res += stack[-1][1]
        return res