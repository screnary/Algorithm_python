# k: any num

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)  # days num
        max_k = k  # max trade num
        if (max_k > n / 2):
            return self.maxProfit_k_inf(prices);
        dp = [[[0, 0] for _ in range(max_k+1)] for _ in range(n+1)]
        for k in range(max_k+1):
            dp[0][k][0] = 0
            dp[0][k][1] = float('-inf')
        for i in range(n+1):
            dp[i][0][0] = 0
            dp[i][0][1] = float('-inf')
        for i in range(1, n+1):  # i /in [1, n]
            for k in range(max_k, 0, -1):  # k /in [1,max_k]
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i-1])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i-1])
        return dp[n][max_k][0]
    
    def maxProfit_k_inf(self, prices):
        n = len(prices)
        if n<2: return 0
        res = 0
        for i in range(n-1):
            if prices[i] < prices[i+1]:
                res += prices[i+1] - prices[i]
        return res
