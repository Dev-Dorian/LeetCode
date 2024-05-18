class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class Solution:
    def maxBinary(self, root):
        if not root:
            return 0
        else:
            return max(self.maxBinary(root.left), self.maxBinary(root.right)) + 1


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.left = TreeNode(7)
    print(Solution().maxBinary(root))
