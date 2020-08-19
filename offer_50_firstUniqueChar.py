from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> str:
        D = defaultdict(lambda: 0)
        for char in s:
            D[char] += 1
        for k in D:
            if D[k]==1:
                return k
        # print(D)
        return " "
    
    def firstUniqChar_(self, s: str) -> str:
        dic = collections.OrderedDict()
        for c in s:
            dic[c] = not c in dic
        for k, v in dic.items():
            if v: return k
        return ' '
