# 实现一个计算器 2-3*4+5
def calculate(s: str) -> int:
​
    def helper(s: List) -> int:
        stack = []
        sign = '+'
        num = 0
​
        while len(s) > 0:
            c = s.pop(0)
            if c.isdigit():
                num = 10 * num + int(c)
​
            if (not c.isdigit() and c != ' ') or len(s) == 0:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    # python 除法向 0 取整的写法
                    stack[-1] = int(stack[-1] / float(num))                    
                num = 0
                sign = c
​
        return sum(stack)
    # 需要把字符串转成列表方便操作
    return helper(list(s))


# 通过递归的方式处理括号：
# calculate(3*(4-5/2)-6) = 3  calculate(4-5/2) - 6 = 3  2 - 6 = 0

def calculate(s: str) -> int:
​
    def helper(s: List) -> int:
        stack = []
        sign = '+'
        num = 0
​
        while len(s) > 0:
            c = s.pop(0)
            if c.isdigit():
                num = 10 * num + int(c)
            # 遇到左括号开始递归计算 num
            if c == '(':
                num = helper(s)
​
            if (not c.isdigit() and c != ' ') or len(s) == 0:
                if sign == '+': ...
                elif sign == '-': ... 
                elif sign == '*': ...
                elif sign == '/': ...
                num = 0
                sign = c
            # 遇到右括号返回递归结果
            if c == ')': break
        return sum(stack)
​
    return helper(list(s))