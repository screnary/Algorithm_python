""" 上升下降字符串
"aaaabbbbcccc" ->
"abccbaabccba"
"""

class Solution:
    def sortString(self, s: str) -> str:
        # compute frequency
        bucket = [0]*(ord('z')-ord('a')+1)
        for c in s:
            bucket[ord(c)-ord('a')] += 1
        res = ""
        while len(res) < len(s):
            # increase loop
            for i in range(len(bucket)):
                if bucket[i] > 0:
                    res += chr(i+ord('a'))
                    bucket[i] -= 1
            # decrease loop
            for i in range(len(bucket)-1, -1, -1):
                if bucket[i] > 0:
                    res += chr(i+ord('a'))
                    bucket[i] -= 1
        return res