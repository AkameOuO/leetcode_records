class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        l = sorted(Counter(arr).values(),reverse=True)
        while l:
            k -= l[-1]
            if k < 0:
                return len(l)
            l.pop()
        return 0