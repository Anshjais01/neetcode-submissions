class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price=0
        min_price=prices[0]
        for sell in prices:
            max_price=max(max_price,sell-min_price)
            min_price=min(min_price,sell)
        return max_price
        