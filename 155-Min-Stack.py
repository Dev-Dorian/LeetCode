class Solution:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        val = min(val, self.minStack[-1]
                  if self.minStack
                  else val)
        self.minStack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]


if __name__ == "__main__":
    stack = Solution()
    print([
        stack.__init__(),
        stack.push(-2),
        stack.push(0),
        stack.push(-3),
        stack.getMin(),
        stack.pop(),
        stack.top(),
        stack.getMin()])
