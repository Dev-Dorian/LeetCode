class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class Solution:
    def isSame(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        # if p is not None and q is not None:
        #    return p.val == q.val and self.isSame(p.left, q.left) and self.isSame(p.right, q.right)
        if p.val != q.val:
            return False
        left = self.isSame(p.left, q.left)
        right = self.isSame(p.right, q.right)
        if left and right:
            return True
        else:
            return False

        # return False


if __name__ == "__main__":
    root1, root1.left, root1.right = TreeNode(1), TreeNode(2), TreeNode(3)
    root2, root2.left, root2.right = TreeNode(1), TreeNode(2), TreeNode(3)
    print(Solution().isSame(root1, root2))
