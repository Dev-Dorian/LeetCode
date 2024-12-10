class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ans = 0
    i = 0

    def kthSmallest(self, root, k):
        if not root:
            return
        self.kthSmallest(root.left, k)
        self.i += 1
        if self.i == k:
            self.ans = root.val
        self.kthSmallest(root.right, k)
        return self.ans


if __name__ == "__main__":
    #       3
    #      / \
    #     1   4
    #      \
    #       2

    # root = TreeNode(3)
    # root.right = TreeNode(4)
    # root.left = TreeNode(1, TreeNode(1), TreeNode(2))

    #          5
    #         / \
    #        3   6
    #      /  \
    #     2    4
    #    /
    #   1

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)

    k = 3

    result = Solution().kthSmallest(root, k)
    print(result)
