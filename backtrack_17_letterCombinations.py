"""
电话号码的字母组合
1, 构建数字-字母对应哈希表
2，顺序遍历数字，用“start”控制当前要遍历的位置
深度优先，一直到叶子才会逐步回退
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        res = []
        digit_map = {'2': ['a','b','c'],
                     '3': ['d','e','f'],
                     '4': ['g','h','i'],
                     '5': ['j','k','l'],
                     '6': ['m','n','o'],
                     '7': ['p','q','r','s'],
                     '8': ['t','u','v'],
                     '9': ['w','x','y','z']}

        def backtrack(path, digits, start):
            nonlocal res
            # path is the decision path, a string ""
            if len(path)==len(digits):
                res.append(path)
            for i in range(start, len(digits)):
                d = digits[i]
                for c in digit_map[d]:
                    path += c
                    backtrack(path, digits, i+1)
                    path = path[:-1]
        backtrack("", digits, 0)
        return res
