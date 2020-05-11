""" 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回 s 所有可能的分割方案。
"""

class Solution:
   def partition(self, s: str) -> List[List[str]]:
        self.res = []
        # construct dp[i][j], n*n size: bool, if str[i:j+1] is Palindrome
        length = len(s)
        dp = [[False for _ in range(length)] for _ in range(length)]
        # all the sub str len
        for l in range(1, length+1):
            # from each index
            for i in range(0, length-l+1):
                j = i + l - 1
                dp[i][j] = s[i]==s[j] and (l<3 or dp[i+1][j-1])
        
        # dfs the decision tree
        def dfs_helper(s, start, dp, tmp):
            # start: sub string start index
            if start == len(s):
                self.res.append(tmp[:])  # list should deep copy, for stable result
            # all the choices
            for i in range(start, len(s)):
                if dp[start][i]:
                    # update choice
                    left = s[start : i+1]
                    tmp.append(left)
                    # go deeper
                    dfs_helper(s, i+1, dp, tmp)
                    # remove choice
                    tmp.pop()

        dfs_helper(s, 0, dp, [])
        return self.res


if __name__ == '__main__':
    app = Solution()
    res = app.partition("aab")
    print(res)
