class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        heap = []
        c = Counter()
        res = []
        for n,f in zip(nums,freq):
            c[n] -= f
            heappush(heap, (c[n],n))
            x, y = heappop(heap)
            while c[y] != x:
                x, y = heappop(heap)
            heappush(heap, (x,y))
            res.append(-x)
                
        return res