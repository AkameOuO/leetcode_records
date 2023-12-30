class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        c = Counter("".join(words))
        l = len(words)
        return all(map(lambda x: x%l == 0,c.values()))
        # for v in c.values():
        #     if v % l != 0:
        #         return False
        