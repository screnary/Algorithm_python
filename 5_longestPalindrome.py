"""最长回文子串
DP
状态：“一个回文去掉两头，仍是回文”
    原字符串的子串是否为回文
    C[i][j] 表示 子串 s[i:j+1]是否为回文
转移方程：
if s[i] == s[j]:
    if j - i < 3:
        C[i][j] = True
    else:
        C[i][j] = C[i+1][j-1]
else:
    C[i][j] = False
"""

class Solution:
    def longestPalindrome(self, s):
        """
        input:
            s: str
        output:
            res: str
        """
        n = len(s)
        if n < 2:
            return s

        C = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            C[i][i] = True
        
        maxlen = 1  # init has length 1
        start = 0
        
        for j in range(1, n):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i >= 3:
                        C[i][j] = C[i+1][j-1]
                    else:
                        C[i][j] = True
                else:
                    C[i][j] = False
                # update the saved str
                if C[i][j] == True:
                    if maxlen < j-i+1:
                        maxlen = j-i+1
                        start = i
        
        return s[start : start + maxlen]
    
    def longestPalindrome_spread(self, s):
        n = len(s)
        if n < 2:
            return s
        
        maxstr = s[0]
        maxlen = 1
        
        def center_spread(s, left, right):
            i = left
            j = right
            if right >= len(s):
                j = right-1
            while i >= 0 and j < len(s):
                if s[i] == s[j]:
                    i -= 1
                    j += 1
                else:
                    break
            return s[i+1:j], j-(i+1)

        for i in range(n):
            odd_s, odd_len = center_spread(s, i, i)
            even_s, even_len = center_spread(s, i, i+1)
            if maxlen < odd_len or maxlen < even_len:
                if odd_len >= even_len:
                    maxstr = odd_s
                    maxlen = odd_len
                else:
                    maxstr = even_s
                    maxlen = even_len
        
        return maxstr


if __name__ == '__main__':
    text = "babad"
    sol = Solution()
    res = sol.longestPalindrome_spread(text)
    print(res)
