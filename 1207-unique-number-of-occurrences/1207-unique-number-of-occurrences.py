class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(l:=list(Counter(arr).values())) == len(set(l))