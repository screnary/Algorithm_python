"""
请你来实现一个 atoi 函数，使其能将字符串转换成整数。
首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。
当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。
注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。
在任何情况下，若函数不能进行有效的转换时，请返回 0。
说明：
假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。
"""
import pdb

class Solution:
    def myAtoi(self, string):
        """
        input:
            string: str
        output:
            num: int, in [-2^31, 2^31 -1]
        """
        res = 0
        ndict = {str(d):d for d in range(10)}
        string = string.lstrip(' ')

        if len(string)<1:
            return 0
        if (string[0] not in ['+', '-'] and string[0] not in ndict):
            return 0

        sign = 1
        if string[0] == '-':
            sign = -1
            string = string[1:]
        elif string[0] == '+':
            string = string[1:]

        boundary = (1<<31)-1 if sign > 0 else (1<<31)
        i = 0
        while i < len(string) and string[i] in ndict:
            char = string[i]
            digit = ndict[char]
            # pdb.set_trace()
            res = res*10 + digit
            i += 1
            if res > boundary:
                return sign * boundary
        return sign * res


if __name__ == '__main__':
    st = '    -41wejiog'
    sol = Solution()
    res = sol.myAtoi(st)
    print(res)
