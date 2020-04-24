""" 
1143, the length of LCS
Dynamic Programming
关键的状态转移：
    C[i,j] = C[i-1, j-1] + 1, if x[i]==y[j]
    C[i,j] = max(C[i,j-1], C[i-1,j]), if x[i] != y[j]
边界条件: i==0 or j==0, C[i,j]=0
    C size (len(text1)+1, len(text2)+1)
"""

class Solution:
    def longestCommonSubsequence(self, text1, text2):
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
        for i in range(1, m+1):
            for j in range(1, n+1):
                assert i > 0
                if text1[i-1] == text2[j-1]:
                    C[i][j] = C[i-1][j-1] + 1
                else:
                    C[i][j] = max(C[i][j-1], C[i-1][j])
        
        return C[m][n], C

    def printOneLCS(self, text1, text2, C):
        m = len(text1)
        n = len(text2)
        i, j = m, n
        csq = ""
        while i > 0 and j > 0:
            if text1[i-1] == text2[j-1]:
                csq = text1[i-1] + csq
                i -= 1
                j -= 1
            else:
                if C[i][j-1] >= C[i-1][j]:
                    j -= 1  # search left
                else:
                    i -= 1  # search up
        print(csq)
    
    def printAllLCS(self, text1, text2, C, i, j, csq):
        while i > 0 and j > 0:
            if text1[i-1] == text2[j-1]:
                csq = text1[i-1] + csq
                i -= 1
                j -= 1
            else:
                if C[i][j-1] > C[i-1][j]:
                    j -= 1
                elif C[i][j-1] < C[i-1][j]:
                    i -= 1
                else:
                    assert C[i][j-1] == C[i-1][j]
                    self.printAllLCS(text1, text2, C, i, j-1, csq)
                    self.printAllLCS(text1, text2, C, i-1, j, csq)
                    return  # finish search form this starting location, terminate this loop
        print(csq)


if __name__ == '__main__':
    text1 = "BDCABA"
    text2 = "ABCBDAB"
    sol = Solution()
    res, C = sol.longestCommonSubsequence(text1, text2)
    print(res)
    [print(C[i]) for i in range(len(text1)+1)]
    sol.printAllLCS(text1, text2, C, len(text1), len(text2), "")
    
