class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root):

        def isValidAux(node, left, right):
            if not node:
                return True
            if node.val <= left or node.val >= right:
                return False

            return (
                isValidAux(node.left, left, node.val) and isValidAux(
                    node.right, node.val, right)
            )
        return isValidAux(root, float('-inf'), float('inf'))


if __name__ == "__main__":
    #       2
    #      / \
    #     1   3

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    #          5
    #         / \
    #        1   4
    #           /  \
    #          3    6

    # root = TreeNode(5)
    # root.left = TreeNode(1)
    # root.right = TreeNode(4)
    # root.right.left = TreeNode(3)
    # root.right.right = TreeNode(6)

    result = Solution().isValidBST(root)
    print(result)
