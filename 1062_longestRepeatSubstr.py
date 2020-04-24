"""
1062 最长重复子串
输出最长重复子串的长度， 若不存在，输出 0
"""

class Solution:
    def longestRepeatingSubstring(self, S):
        """ binary search by string length """
        n = len(S)
        left, right = 1, n
        while left <= right:
            L = left + (right - left)//2  # new substring length, need to check
            if self.__check(S, L) == -1:
                right = L-1  # if not exist L length, reduce the right bound (sup of Length)
            else:
                left = L+1  # if exist, increase the left bound (under bound of Length)
        return left-1  # (mid, L is the result, L=left-1)
        

    def __check(self, S, L):
        """search a substring of given length
            that occurs at least 2 times
        if exists, return start position;
        if not, return -1
        """
        seen = set()
        n = len(S)
        for i in range(n - L + 1):
            tmp = S[i : i+L]
            if tmp in seen:
                return i
            seen.add(tmp)
        return -1


    def longestRepeatingSubstring_slow(self, S):
        """ Too slow O(N^3)
        input:
            S: str
        output:
            res: int
        """
        if len(S) < 2:
            return 0
        size = len(S)
        max_len = 1
        for i in range(0, size-2):
            for j in range(i+1, size-1):
                # print(S[i:j+1], end=" ")
                if self.__valid(S, i, j):
                    # print('repeated')
                    print(S[i:j+1])
                    cur_len = j-i+1
                    if max_len < cur_len:
                        max_len = cur_len
                # print('')
        if max_len == 1:
            return 0
        return max_len
                
    def __valid(self, S, left, right):
        shift = 1
        flag = False
        while shift <= len(S) - 1 - right:
            for idx in range(left, right+1):
                if S[idx] != S[idx+shift]:
                    break  # if not equal, check next shift
                elif idx == right:
                    return True  # if completely equal, return True
            shift += 1
        return flag
    
    def longestDupSubstring(self, S):
        """ 
        return the substring
        """
        n = len(S)
        left, right = 1, n
        flag = 0
        while left <= right:
            L = left + (right-left)//2
            start = self.__check(S, L)
            if start != -1:
                left = L+1
                flag = start
            else:
                right = L-1
        if left-1 == 0:
            return ""
        return S[flag: flag+L]


if __name__ == "__main__":
    sol = Solution()
    s = "bbccbbcc"
    num = sol.longestRepeatingSubstring(s)
    print(num)
    st = sol.longestDupSubstring(s)
    print(st)
