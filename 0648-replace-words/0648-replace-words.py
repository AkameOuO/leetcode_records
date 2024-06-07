class Trie:
    def __init__(self):
        self.end = False
        self.trie = defaultdict(Trie)
        
    def add(self, s):
        if not s:
            self.end = True
            return
        n = s.pop()
        self.trie[n].add(s)
    
    def get(self,s):
        if self.end:
            return ""
        if not s or s[-1] not in self.trie:
            return None
        n = s.pop()
        t = self.trie[n].get(s)
        if t is None:
            return None
        else:
            return n+t
            
    def __repr__(self):
        return str({
            "end":self.end,
            "trie":self.trie
        })
        
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.add(list(word)[::-1])
        words = sentence.split()
        # print(trie.trie["m"])
        # print(trie.get(list("miszkays")[::-1]))
        # print(sorted(words, key=lambda x:(len(x), x)))
        res = []
        for word in words:
            t = trie.get(list(word)[::-1])
            res.append(t or word)
        return " ".join(res)