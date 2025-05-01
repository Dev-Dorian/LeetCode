""" 
FUNCTION preorderTraversal(root):
    // 'root' is the root of the binary tree
    results = EMPTY_LIST

    FUNCTION traverse(node):
        IF node IS NOT NULL THEN
            ADD node.value TO results
            traverse(node.left)
            traverse(node.right)
        END_IF
    END_FUNCTION

    traverse(root)
    RETURN results
END_FUNCTION """

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution():
    def preorderTraversal(self, root):
        ans = []

        def dfs(root):
            if root is None:
                return
            ans.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ans


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(Solution().preorderTraversal(root))
