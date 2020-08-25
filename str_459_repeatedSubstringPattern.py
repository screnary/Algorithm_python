"""
重复的子字符串
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。
给定的字符串只含有小写英文字母，并且长度不超过10000。

可以考虑双倍字符串，利用循环节，进行 find
"""

class Solution:
    def repeatedSubstringPattern(self, s):
        """ input| s: str
           output| bool
        """
        # enumerate all the possible len of substrings
        n = len(s)
        for m in range(1, n//2+1):
            if n % m == 0:
                if all(s[i]==s[i-m] for i in range(m, n)):
                    return True
        return False
