class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution():
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        if abs(self.getHeight(root.left) - self.getHeight(root.right)) > 1:
            # print(self.getHeight(root.left))
            # print(self.getHeight(root.right))
            # print(self.getHeight(root.left) - self.getHeight(root.right) > 1)
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def getHeight(self, node):
        if node is None:
            return 0
        # print(max(self.getHeight(node.left), self.getHeight(node.right)) + 1)
        return max(self.getHeight(node.left), self.getHeight(node.right)) + 1


if __name__ == "__main__":
    solution = Solution()

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))

    # Check if the tree is height-balanced
    print(solution.isBalanced(root))  # Output: True
