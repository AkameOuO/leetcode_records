class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        mc = None
        for c in map(Counter, words):
            if mc is None:
                mc = c
                continue
            for k in list(mc.keys()):
                if k not in c:
                    del mc[k]
                else:
                    mc[k] = min(mc[k], c[k])
        r = []
        for k, v in mc.items():
            r += [k] * v
        return r