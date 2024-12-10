from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution():
    def minDepth(self, root):
        if root is None:
            return 0
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1

    # DFS
    def minDepth1(self, root):
        if not root:
            return 0
        if None in [root.left, root.right]:
            return max(self.minDepth1(root.left), self.minDepth1(root.right)) + 1
        else:
            return min(self.minDepth1(root.left), self.minDepth1(root.right)) + 1

    # BFS
    def minDepth2(self, root):
        if not root:
            return 0
        queue = deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if node:
                if not node.left and not node.right:
                    return level
                else:
                    queue.append((node.left, level+1))
                    queue.append((node.right, level+1))


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(20, TreeNode(3), TreeNode(40)))

    print(Solution().minDepth(root))
