class Solution:
    def minOperations(self, k: int) -> int:
        for i in count(1):
            if i * i >= k:
                return (i-1) * 2
            if i * (i+1) >= k:
                return (i-1) * 2 + 1