class Trie:
    def __init__(self):
        self.data = (float("inf"),float("inf"))
        self.trie = defaultdict(Trie)
        
    def add(self, s, index):
        data = (len(s), index)
        if data < self.data:
            self.data = data
        if not s:
            return
        n = s.pop()
        self.trie[n].add(s, index)
    
    def get(self,s):
        if not s or s[-1] not in self.trie:
            return self.data[1]
        n = s.pop()
        return self.trie[n].get(s)
            
    def __repr__(self):
        return str({
            "data":self.data,
            "trie":self.trie
        })
        
class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = Trie()
        for word,i in zip(wordsContainer,count()):
            trie.add(list(word), i)
        return [trie.get(list(word)) for word in wordsQuery]
            