class Solution:
    def minimizeStringValue(self, s: str) -> str:
        c = Counter(s)
        for ch in ascii_lowercase:
            c[ch] += 1
        target = c["?"]
        del c["?"]
        heap = [(v,k) for k,v in c.items()]
        heapify(heap)
        l = []
        for _ in range(target):
            v,k = heappop(heap)
            l.append(k)
            heappush(heap,(v+1,k))
        l.sort(reverse=True)
        return "".join([ch if ch != "?" else l.pop() for ch in s])