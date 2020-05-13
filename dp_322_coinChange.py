""" 零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。
编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1

dp[n] = dp[n - coin] + 1, for coin in coins
"""

class Solution:
    def coinChange(coins, amount):
        """ input| coins: List[int], amount: int
           output| coin_num: int
        """
        # init dp table
        dp = [amount+1] * (amount+1)
        dp[0] = 0  # boundary case

        for i in range(1, amount+1):
            for coin in coins:
                if i - coin < 0:
                    continue  # skip invalid case
                dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[amount] if dp[amount] != amount+1 else -1
