# sliding window

import pdb

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # sliding window
        L, n = len(needle), len(haystack)
        for start in range(n - L + 1):
            if haystack[start:start+L] == needle:
                return start
        return -1

    def strStr_twoPointers(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        i = 0
        for i in range(len(haystack)):
            for j in range(len(needle)):
                if i+j == len(haystack):
                    return -1
                elif needle[j]!=haystack[i+j]:
                    break
                elif j == len(needle)-1:
                    return i
        return -1


if __name__ == '__main__':
    sol = Solution()
    haystack = "mississippi"
    needle = "issip"
    res = sol.strStr(haystack, needle)
    print(res)
