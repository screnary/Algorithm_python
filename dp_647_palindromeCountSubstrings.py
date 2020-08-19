""" 回文子串
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

DP
dp[i][j]: 从i开始，到j结束的子串是否回文
对角线均为 True，
然后逐渐增加宽度（从对角线）
"""

class Solution:
    def countSubstrings(self, s):
        """ input| s: str
           output| int (i.e. num of palindrome sub strs) """
        n = len(s)
        if n <= 1:
            return n

        dp = [[False]*n for _ in range(n)]
        # initialization
        for i in range(n):
            dp[i][i] = True

        count = n
        # expand from the diagnal, fill the dp chart
        for j in range(1, n):  # col
            for i in range(0, j):  # row
                if s[i]==s[j]:
                    if j-i <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
                if dp[i][j]:
                    count += 1
        return count        
