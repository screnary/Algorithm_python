"""
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。

来源：力扣（LeetCode） 链接：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "None"
        ls = self.serialize(root.left)
        rs = self.serialize(root.right)
        # post operation for preorder str
        serial = str(root.val) + ',' + ls + ',' + rs
        return serial

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def redeserialize(l_data):
            if l_data[0] == 'None':
                l_data.pop(0)
                return None
            # preorder construct
            root = TreeNode(int(l_data[0]))
            l_data.pop(0)
            # traverse children
            root.left = redeserialize(l_data)
            root.right = redeserialize(l_data)
            return root
        
        l_data = data.split(",")
        root = redeserialize(l_data)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))