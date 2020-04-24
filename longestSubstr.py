class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        ptr_h: header pointer
        ptr_t: tail pointer
        将不重复子串全部存到一个set中
        800 ms
        """
        # visit the input string, two pointers, keep a substr set
        if s == '':
            return 0

        res = set()
        for ptr_h in range(len(s)):
            ptr_t = ptr_h + 1
            cur_s = s[ptr_h:ptr_t]
            # extend cur_s
            extend_flag = True
            while extend_flag and ptr_t < len(s):
                ptr_t += 1
                if s[ptr_t-1] in cur_s:
                    extend_flag = False
                else:
                    cur_s = s[ptr_h:ptr_t]
            if cur_s not in res:
                res.add(cur_s)
        print(res)
        return max([len(substr) for substr in res])

    def lengthOfLongestSubstring_1(self, s: str) -> int:
        """
        ptr_h: header pointer
        ptr_t: tail pointer
        使用队列，sliding window
        92 ms
        """
        # visit the input string, two pointers, keep a substr set
        if s == '':
            return 0

        res = []
        max_len = 0
        cur_len = 0
        for i in range(len(s)):
            cur_len += 1
            while s[i] in res:
                res.pop(0)
                cur_len -= 1
            if cur_len > max_len: max_len = cur_len
            res.append(s[i])
        return max_len


if __name__ == '__main__':
    input_str = 'pwwkew'
    app = Solution()
    print(app.lengthOfLongestSubstring_1(input_str))
