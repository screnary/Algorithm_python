"""
你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。

空节点则用一对空括号 "()" 表示。而且你需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-string-from-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if t is None:
            return ''
        ls = self.tree2str(t.left)  # left str
        rs = self.tree2str(t.right)  # right str
        if rs != '': 
            pres = str(t.val) + '(' + ls + ')' + '(' + rs + ')'
        elif ls != '':
            pres = str(t.val) + '(' + ls + ')'
        else:
            pres = str(t.val)
        return pres  # pre order str
