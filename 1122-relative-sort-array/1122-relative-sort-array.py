class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.sort(key=lambda x:arr2.index(x) if x in arr2 else 10000+x)
        return arr1