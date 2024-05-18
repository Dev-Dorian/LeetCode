class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Morris Traversal Solution


class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        result, prev, cur = [], None, root
        while cur:
            if cur.left is None:
                result.append(cur.val)
                prev = cur
                cur = cur.right
            else:
                node = cur.left
                while node.right and node.right != cur:
                    node = node.right

                if node.right is None:
                    node.right = cur
                    cur = cur.left
                else:
                    result.append(cur.val)
                    node.right = None
                    prev = cur
                    cur = cur.right

        return result


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    result = Solution().inorderTraversal(root)
    print(result)
