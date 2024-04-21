prime = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97}
class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        l = []
        for i, n in zip(count(), nums):
            if n in prime:
                l.append(i)
        return l[-1] - l[0]