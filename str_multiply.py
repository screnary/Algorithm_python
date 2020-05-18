class Solution:
    """
    Leetcode No.43. String Multiply
    352 ms
    13.7 MB
    """
    def multiply(self, num1: str, num2: str) -> str:
        if num1 is '0' or num2 is '0':
            return '0'
        if len(num1) < len(num2):
            num2, num1 = num1, num2
        res = '0'
        for i, digit in enumerate(num2[::-1]):
            p = int(digit)
            carry = 0
            mul = ''
            for j, digit_base in enumerate(num1[::-1]):
                q = int(digit_base)
                temp = (p * q + carry) % 10
                carry = (p * q + carry) // 10
                mul = str(temp) + mul
            if carry > 0:
                mul = str(carry) + mul
            mul = mul + '0'*i
            res = self.strplus(res, mul)
        return res

    def strplus(self, x, y):
        lx = len(x)
        ly = len(y)
        if len(x) < len(y):
            x, y = y, x
            lx, ly = ly, lx
        x = x[::-1]
        y = y[::-1] + '0'*(len(x)-len(y))
        carry = 0
        sum = ''
        for i in range(len(y)):
            p = int(y[i])
            q = int(x[i])
            temp = (p + q + carry) % 10
            carry = (p + q + carry) // 10
            sum = str(temp) + sum
        if carry > 0:
            sum = str(carry) + sum
        return sum


if __name__ == '__main__':
    a = '12345'
    b = '67'
    app = Solution()
    print(app.multiply(a, b))
    print(app.strplus(a, b))
