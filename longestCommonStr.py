""" 
1143, the length of LCString
Dynamic Programming
关键的状态转移：
    C[i,j] = C[i-1, j-1] + 1, if x[i]==y[j]
    C[i,j] = 0, if x[i] != y[j]
边界条件: i==0 or j==0, C[i,j]=0
    C size (len(text1)+1, len(text2)+1)
"""

class Solution:
    def longestCommonSubstring(self, text1, text2):
        """
        input:
            text1: str
            text2: str
        output:
            res: int
        """
        m, n = len(text1), len(text2)
        if m+n == 0:
            return 0
        C = []
        for j in range(0, m+1):
            C.append([0]*(n+1))
        maxlen = 0
        loc_flag = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    C[i][j] = C[i-1][j-1] + 1
                    if maxlen < C[i][j]:
                        maxlen = C[i][j]
                        loc_flag = j
                else:
                    C[i][j] = 0

        substr = text2[loc_flag-maxlen : loc_flag]
        return maxlen, substr


if __name__ == '__main__':
    text1 = "BDCABA"
    text2 = "ABCBDAB"
    sol = Solution()
    res, substr = sol.longestCommonSubstring(text1, text2)
    print(res)
    print(substr)
