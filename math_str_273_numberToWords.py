""" 整数转换英文表示
思路：三个三个为一组，生成英文描述单元「Five Hundred Twenty Four」，然后在后面添加“单位”：「个(省略)，千，百万，十亿」
"""

class Solution:
    def numberToWords(self, num):
        """ input| num: int
           output| str
        """
        if num == 0:
            return 'Zero'

        digits = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten',
                  11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen',
                  18:'Eighteen', 19:'Nineteen', 20:'Twenty', 30:'Thirty', 40:'Forty', 50:'Fifty', 60:'Sixty', 70:'Seventy',
                  80:'Eighty', 90:'Ninety'}        

        def helper(num, grade):
            # num < 1000
            hundred, tenth = divmod(num, 100)
            res = ""
            if num==0: return ""
            if tenth > 0 and tenth < 20:
                res = digits[tenth]
            elif tenth >= 20:
                n, r = divmod(tenth, 10)
                if r == 0:
                    res = digits[tenth]
                else:
                    res = digits[n*10] + ' ' + digits[r]
            if hundred > 0 and tenth > 0:
                res = digits[hundred] + ' Hundred ' + res
            elif hundred > 0 and tenth == 0:
                res = digits[hundred] + ' Hundred'
            return res + " " + grade if grade != "" else res

        grades = ['', 'Thousand', 'Million', 'Billion']
        res = ""
        while num > 0 and grades:
            grade = grades.pop(0)
            num, remainder = divmod(num, 1000)
            numstr = helper(remainder, grade)
            if numstr != '':
                if grade != '' and res != '':
                    res = numstr + ' ' + res
                else:
                    res = numstr
        return res


if __name__ == '__main__':
    sol = Solution()
    res = sol.numberToWords(123000)
    print(res)
