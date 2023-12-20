class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        heapify(prices)
        a = heappop(prices) + heappop(prices)
        return money if a>money else money-a