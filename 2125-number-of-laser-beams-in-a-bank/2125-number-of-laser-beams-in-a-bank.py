class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        last = 0
        res = 0
        for r in bank:
            c = Counter(r)["1"]
            if c == 0:
                continue
            res += last * c
            last = c
        return res