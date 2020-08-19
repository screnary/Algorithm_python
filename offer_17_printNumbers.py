class Solution:
    def printNumbers(self, n):
        maxnum = 9
        for i in range(n-1):
            maxnum = maxnum*10 + 9
        return [num for num in range(1,maxnum+1)]


if __name__=="__main__":
    app = Solution()
    res = app.printNumbers(3)
    print(res)
