""" 通过删除字母匹配到字典里最长单词
给定一个字符串和一个字符串字典，找到字典里面最长的字符串，该字符串可以通过删除给定字符串的某些字符来得到。
如果答案不止一个，返回长度最长且字典顺序最小的字符串。如果答案不存在，则返回空字符串。

思路：
1，将字典进行排序，由长到短（因为要求返回最长的匹配，方便之后的遍历）
2，匹配是一个顺序遍历比较的流程
"""

class Solution:
    def findLongestWord(self, s, d):
        """ input| s: str, d: List[str]
           output| str
        """
        d_sort = sorted(d)  # sort by secondary key
        d_sort = sorted(d_sort, key=lambda s: len(s), reverse=True)  # sort by primary key

        len_s = len(s)
        for ds in d_sort:
            len_ds = len(ds)
            if len_s >= len_ds:
                i, j = 0, 0
                while i < len_s and j < len_ds:                 
                    if s[i] == ds[j]:
                        i += 1
                        j += 1
                    else:
                        i += 1
                if j == len_ds:  # check if ds is fully compared
                    return ds
        return ""
            