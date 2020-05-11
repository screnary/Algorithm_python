"""
生成字符串，由 n 对括号组成：
输出满足括号规则的所有括号组合。
即：
生成 长为 2n 的字符串，
1）每个"(" 之后都有一个 ")"与之配对相消，
2）每个")" 前面必然有至少一个还没有配对的 "("

构建深度为 2n 的决策树，每个节点的选择集合 {"(", ")"}, 在选择时考虑合法性来剪枝
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(path, left, right):
            nonlocal res
            # terminate condition
            if len(path) == 2*n:
                res.append("".join(path))
            # make choice in choice space
            if left < n:
                path.append('(')
                backtrack(path, left+1, right)
                path.pop()
            if right < left:
                path.append(')')
                backtrack(path, left, right+1)
                path.pop()
        backtrack([], 0, 0)
        return res
            