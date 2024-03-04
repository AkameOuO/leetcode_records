class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        s = 0
        res = 0
        deq = deque(sorted(tokens))
        while deq:
            if power < deq[0]:
                if s <= 0:
                    break
                power += deq.pop()
                s -= 1
            else:
                power -= deq.popleft()
                s += 1
            res = max(res,s)
        return max(res,0)