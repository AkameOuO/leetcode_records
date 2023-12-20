class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        heapify(prices)
        a,b = heappop(prices),heappop(prices)
        return money if a+b>money else money-a-b