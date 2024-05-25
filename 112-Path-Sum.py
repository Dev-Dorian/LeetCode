class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution():
    def isPathSum(self, root: TreeNode, targetSum) -> bool:
        def dfs(node, sum):
            if not node:
                return False
            sum += node.val
            if not node.left and not node.right:
                return sum == targetSum
            return (dfs(node.left, sum) or
                    dfs(node.right, sum))
        return dfs(root, 0)


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.right = TreeNode(2)

    print(Solution().isPathSum(root, 22))
