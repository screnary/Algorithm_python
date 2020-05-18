"""
你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。
给定一个数字 n，找出可形成完整阶梯行的总行数。
n 是一个非负整数，并且在32位有符号整型的范围内。
"""

class Solution:
    def arrangeCoins(self, n: int) -> int:
        """ input| n: int
           output| int
        """
        # do the math
        k = (2*n + 0.25) ** 0.5 - 0.5
        return int(k)

    def biSec(self, n):
        # bisec search k
        l, r = 1, int((2*n)**0.5)+1  # if n==1, l=1, make sure r=2>l
        while l < r:
            mid = (l + r) // 2
            tmpsum = (mid+1) * mid / 2
            print(mid, tmpsum)
            if tmpsum == n:
                return mid
            elif tmpsum > n:
                r = mid
            elif tmpsum < n:
                l = mid + 1
        return l-1  # here, l==r, tmpsum(r)>n
