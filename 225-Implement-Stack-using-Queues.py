from collections import deque


class Solution:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q.append(x)

    def pop(self):
        """
        :rtype: int
        """
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())
        return self.q.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.q[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q) == 0


if __name__ == "__main__":
    stack = Solution()
    print([
        stack.__init__(),
        stack.push(1),
        stack.push(2),
        stack.top(),
        stack.pop(),
        stack.empty()])
