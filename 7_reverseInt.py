"""
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""

class Solution:
    def reverse(self, x):
        """ input: x Int
            output: Int
        """
        res = 0
        sign = -1 if x < 0 else 1
        boundary = 1<<31 if x < 0 else (1<<31) - 1
        num = sign * x
        while num > 0:
            d = num % 10
            res = res*10 + d
            if res > boundary:
                return 0
            num = num // 10

        return sign*res


if __name__ == '__main__':
    sol = Solution()
    num = 1463847412
    res = sol.reverse(num)
    print(res)
