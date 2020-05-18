import pdb

class Solution:
    def complexNumberMultiply(self, a, b):
        """ input| a: str, b: str
           output| str
        """
        # read num
        def str2num(num_s):
            num = 0
            sign = 1
            for i in range(len(num_s)):
                c = num_s[i]
                if c.isdigit():
                    num = num*10 + int(c)
                elif c=='-':
                    sign = -1
            return sign * num

        complex_a = [str2num(s) for s in a.split("+")]
        complex_b = [str2num(s) for s in b.split("+")]
        
        real = complex_a[0]*complex_b[0] - complex_a[1]*complex_b[1]
        imaginary = complex_a[0]*complex_b[1] + complex_a[1]*complex_b[0]
        
        res = str(real) + "+" + str(imaginary) + 'i'
        return res


if __name__ == '__main__':
    a = "78+-76i"
    b = "-86+72i"
    sol = Solution()
    res = sol.complexNumberMultiply(a, b)
    print(res)
