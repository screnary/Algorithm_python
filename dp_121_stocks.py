class Solution:
    def maxProfit(self, prices):
        """ 121.
            input| prices: List[int]
           output| int
        """
        n = len(prices)
        if n==0: return 0
        min_price = float('inf')
        max_profit = 0

        for p in prices:
            min_price = min(min_price, p)
            max_profit = max(max_profit, p - min_price)
        return max_profit
    
    def maxProfit_multi(self, prices):
        """ 122.
            input| prices: List[int]
           output| int
        """
        n = len(prices)
        if n<2: return 0
        res = 0
        for i in range(n-1):
            if prices[i] < prices[i+1]:
                res += prices[i+1] - prices[i]
        return res
