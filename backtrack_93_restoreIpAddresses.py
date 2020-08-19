"""
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。

坑：
每段区域不能有前导0: "01", "012", "00", etc.
"""

class Solution:
    def restoreIpAddresses(self, s):
        """ input| s: str
           output| List[str]
        """
        n = len(s)
        res = []
        def backtrack(start, remain, path):
            nonlocal res
            # terminate
            if remain == 0:
                # finished placement of 3 dots
                if n-start>0 and n-start<=3:  # all num has been recorded
                    cur = s[start:n]
                    if cur[0]=='0' and len(cur)>1:
                        return
                    if int(cur) >= 0 and int(cur) <= 255:
                        res.append('.'.join(path+[cur]))
                return
            # make choice
            for l in range(1,4):
                if start + l <= n:  # if not reach end
                    cur = s[start:start+l]
                    if cur[0]=='0' and len(cur)>1:
                        return
                    if int(cur) >= 0 and int(cur) <= 255:
                        backtrack(start+l, remain-1, path+[cur])
                else:
                    return

        backtrack(0, 3, [])
        return res


if __name__=="__main__":
    app = Solution()
    string = "25525511135"
    res = app.restoreIpAddresses(string)
    print(res)
