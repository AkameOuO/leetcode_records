class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for i in range(1, 61):
            tmp = num1 - num2 * i
            if tmp < i:
                return -1
            ones = Counter(bin(tmp))["1"]
            if ones <= i:
                return i
        return -1
