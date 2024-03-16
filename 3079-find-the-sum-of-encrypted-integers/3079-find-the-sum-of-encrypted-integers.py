class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        return sum(map(lambda x:int(max(str(x))*len(str(x))),nums))