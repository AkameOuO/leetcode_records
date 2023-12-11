class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        q = len(arr) // 4 #ceil((len(arr)-1) / 4)
        print(q)
        for i in range(len(arr)-q):
            if arr[i] == arr[i+q]:
                return arr[i]