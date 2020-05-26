""" stack_150_reversePoland
输入: ["4", "13", "5", "/", "+"]
输出: 6
解释: (4 + (13 / 5)) = 6
"""
import math

class Solution:
    def evalRPN(self, tokens):
        """ input| tokens: List[str]
           output| int
        """
        n = len(tokens)
        if n==0: return 0  # 特殊情况处理
        stack_num = []
        stack_ops = []
        for i in range(n):
            c = tokens[i]
            if c.isdigit() or len(c)>1:
                if c[0]=='-':
                    stack_num.append(-int(c[1:]))  # 负数的处理
                else:
                    stack_num.append(int(c))
            else:  # is operator
                b = stack_num.pop()
                a = stack_num.pop()
                if c == '+':
                    stack_num.append(a + b)
                elif c == '-':
                    stack_num.append(a - b)
                elif c == '*':
                    stack_num.append(a * b)
                elif c == '/':
                    tmp = a/b
                    tmp = math.ceil(tmp) if tmp < 0 else math.floor(tmp)
                    stack_num.append(tmp)  # 注意这里，只保留整数部分
        return stack_num[0]


if __name__ == '__main__':
    sol = Solution()
    # tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    tokens = ["4","13","5","/","+"]
    res = sol.evalRPN(tokens)
    print(res)
