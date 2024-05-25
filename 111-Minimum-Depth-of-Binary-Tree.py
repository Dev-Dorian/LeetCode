class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution():
    def isMinimun(self, root):
        if root is None:
            return 0
        if root.left and root.right:
            return min(self.isMinimun(root.left), self.isMinimun(root.right)) + 1
        else:
            return max(self.isMinimun(root.left), self.isMinimun(root.left)) + 1


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(20, TreeNode(3), TreeNode(40)))

    print(Solution().isMinimun(root))
