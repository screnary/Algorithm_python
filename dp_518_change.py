""" 零钱兑换 II
给定不同面额的硬币 coins 和一个总金额 amount。
写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。

dp[coin][i] = dp[pre_coins][i] (if i < coin)
dp[coin][i] = dp[pre_coins][i] + dp[coin][i-coin] (if i >= coin)
"""

class Solution:
    def coinChange(coins, amount):
        """ input| coins: List[int], amount: int
           output| coin_num: int
        """
        dp = [0] * (amount+1)  # 初始化，使用 0 个硬币，凑出金额的种类
        dp[0] = 1  # 凑出金额 0 的组合种类

        for coin in coins:
            for i in range(amount+1):  # for 0~amount
                if i < coin:
                    continue  # dp[coin][i] = dp[pre_coins][i]
                else:
                    dp[i] = dp[i] + dp[i-coin]  # dp[coin][i] = dp[pre_coins][i] + dp[coin][i-coin]
        return dp[amount]
