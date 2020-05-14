""" 实现字符串中包含：数字，+， -，(， ) 的基本计算器
"1 + 1"

计算：先将所有数字压栈，最后直接对栈内元素求和
"""
import pdb


class Solution:
    def calculate(self, s):
        """ input| s: str
           output| res: int
        """
        def operate(n1, n2, op):
            if op=='+':
                return n1 + n2
            if op=='-':
                return n1 - n2

        def helper(s):
            stack_num = []  # init stack
            stack_op = []
            num = -1  # init the num

            # traverse the input string
            for i in range(len(s)):
                c = s[i]
                # str to int num
                if c.isdigit():
                    if num == -1:
                        num = int(c)
                    else:
                        num = num*10 + int(c)

                if not c.isdigit() and c != " ":
                    if num != -1:  # control when to en-stack
                        stack_num.append(num)
                        num = -1  # reset after num en-stack

                    if c != ')' and (not stack_op or stack_op[-1]=='('):
                        # condition need to care
                        stack_op.append(c)
                    elif c=='(':
                        stack_op.append(c)
                    elif c in ['+', '-']:
                        while stack_op:
                            if stack_op[-1] == '(':
                                break
                            op = stack_op.pop()
                            n2 = stack_num.pop()
                            n1 = stack_num.pop()
                            stack_num.append(operate(n1, n2, op))
                        stack_op.append(c)  # caculation is delayed
                    elif c==')':
                        op = stack_op.pop()
                        while op!='(':
                            n2 = stack_num.pop()
                            n1 = stack_num.pop()
                            stack_num.append(operate(n1, n2, op))
                            op = stack_op.pop()
            # pdb.set_trace()
            if num != -1:
                stack_num.append(num)
            while stack_op:
                op = stack_op.pop()
                n2 = stack_num.pop()
                n1 = stack_num.pop()
                stack_num.append(operate(n1, n2, op))

            return stack_num[0]
        return helper(s)

if __name__ == '__main__':
    s = " 3 * (4 - 5 / 2) - 6"
    s = "(1+(4+5+2)-3)+(6+8)"
    s = "(1)"

    sol = Solution()
    res = sol.calculate(s)
    print(res)
