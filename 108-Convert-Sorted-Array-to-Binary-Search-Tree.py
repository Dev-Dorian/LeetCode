class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        total = len(nums)
        if not total:
            return None
        midle = total // 2
        return TreeNode(
            nums[midle],
            self.sortedArrayToBST(
                nums[:midle]), self.sortedArrayToBST(nums[midle + 1:])

        )
    """  
   def balance(self, nums, left, right):
        while left <= right:
            middle = (left + right) // 2

            node = TreeNode(nums[middle])
            node.left = self.balance(nums, left, middle - 1)
            node.right = self.balance(nums, middle + 1, right)

            return node

        return None

    def sortedArrayToBST(self, nums):
        last = len(nums) - 1
        # print(last)
        return self.balance(nums, 0, last) """


if __name__ == "__main__":
    num = [-10, -3, 0, 5, 9]
    result = Solution().sortedArrayToBST(num)
    print(result.val)
    print(result.left.val)
    print(result.right.val)
