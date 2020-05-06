class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.max_path = 0
        def get_path_len(root):
            if root is None:
                return 0
            len_left = get_path_len(root.left)
            len_right = get_path_len(root.right)

            # post order
            path_left, path_right = 0, 0  # init, if not satisfied
            if root.left and root.val == root.left.val:
                path_left = len_left + 1  # accumulate
            if root.right and root.val == root.right.val:
                path_right = len_right + 1

            self.max_path = max(self.max_path, path_left + path_right)
            return max(path_left, path_right)
        get_path_len(root)
        return self.max_path