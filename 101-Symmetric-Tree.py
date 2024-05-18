class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.mirror(root.left, root.right)

    def mirror(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.val != node2.val:
            return False
        return (node1.val == node2.val and
                self.mirror(node1.left, node2.right) and
                self.mirror(node1.right, node2.left))
