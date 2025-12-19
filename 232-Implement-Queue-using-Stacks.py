class MyQueue(object):

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())
        self.stack_1.append(x)

        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())

    def pop(self):
        """
        :rtype: int
        """
        return self.stack_1.pop()

    def peek(self):
        """
        :rtype: int
        """
        return self.stack_1[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack_1


if __name__ == "__main__":
    stack = MyQueue()
    print([
        stack.__init__(),
        stack.push(1),
        stack.push(2),
        stack.peek(),
        stack.pop(),
        stack.empty()
    ])


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
