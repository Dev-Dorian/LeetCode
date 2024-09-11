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
    stack.push(-2)
    stack.push(0)
    stack.push(3)
    stack.push(100)
    stack.push(-10)
    stack.push(-5)
    stack.push(1)
    stack.push(40)
    stack.pop()
    stack.pop()
    # stack.pop()
    print([stack.top(), stack.getMin()])
