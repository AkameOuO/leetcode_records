class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        for pas, total in classes:
            heappush(heap, ((pas/total - (pas+1)/(total+1)), pas, total))

        for _ in range(extraStudents):
            _, pas, total = heappop(heap)
            pas += 1
            total += 1
            heappush(heap, ((pas/total - (pas+1)/(total+1)), pas, total))
        
        return sum(map(lambda x:(x[1]/x[2]), heap)) / len(heap)
