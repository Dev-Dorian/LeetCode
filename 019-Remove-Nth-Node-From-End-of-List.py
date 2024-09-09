class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self is None:
            return "Nil"
        else:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(-1)
        dummy.next = head
        left = dummy
        right = dummy

        for i in range(n):
            right = right.next

        while right.next:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print(Solution().removeNthFromEnd(head, 2))
