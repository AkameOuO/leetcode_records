class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        c = Counter(nums)
        res = []
        for k,v in c.items():
            for i in range(v):
                try:
                    res[i].append(k)
                except:
                    res.append([k])
        return res