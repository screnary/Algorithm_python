""" 有重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合
先将输入string排序，当前 cur char 未使用时：
进一步检查： cur==pre 且 pre还未使用过，这时说明同级决策树节点已经处理过 相同char，直接剪枝回溯！
"""

class Solution:
    def permutation(self, S: str) -> List[str]:
        self.res = []
        self.S = sorted(S)
        self.visited = [False] * len(S)
        self.num = len(S)
        self.backtrack("")
        return self.res
    
    def backtrack(self, tmp):
        # tmp is string, init ""
        if len(tmp)==self.num:
            self.res.append(tmp)
        for i in range(self.num):
            if not self.visited[i]:
                if i > 0 and self.S[i]==self.S[i-1] and not self.visited[i-1]:
                    continue  # important!
                # make choice
                self.visited[i] = True
                tmp += self.S[i]
                self.backtrack(tmp)
                # remove choice
                self.visited[i] = False
                tmp = tmp[:-1]
