class Solution:
    def totalMoney(self, n: int) -> int:
        return sum(map(lambda x:x//7+x%7+1,range(n)))