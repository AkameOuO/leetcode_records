class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        res = 0
        for r in mat:
            if sum(r) != 1:
                continue
            i = r.index(1)
            if sum(map(lambda x:x[i],mat)) == 1:
                res += 1
        return res