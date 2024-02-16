class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        l = sorted(Counter(arr).items(),key=lambda x:x[1],reverse=True)
        while l:
            k -= l[-1][1]
            if k < 0:
                return len(l)
            l.pop()
        return 0