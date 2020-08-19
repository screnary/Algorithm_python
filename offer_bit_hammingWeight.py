""" 请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。
例如，把 9 表示成二进制是 1001，有 2 位是 1。
因此，如果输入 9，则该函数输出 2。
"""

def tobin_(n):
    if n==0:
        return "0"
    m, r = divmod(n , 2)
    return str(r) + tobin_(m)

def tobin(n):
    if n==0:
        return 0
    m, r = divmod(n , 2)
    return r + tobin(m)

def hammingWeight(self, n: int) -> int:
        res = 0
        while n!=0:
            res += n & 1
            n = n >> 1
        return res

print(tobin(10))