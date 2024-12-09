class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if self:
            return "{}".format(self.val)
        else:
            return None


class Solution:

    def reverseList(self, head):
        current = head
        prev = None
        # current is not None es lo mismo que solo dejar current
        while current is not None:  # !=
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        return prev

    def reverseListRecursive(self, head):
        if not head or not head.next:
            return head
        newHead = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None

        return newHead


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(Solution().reverseList(head))
    print(Solution().reverseListRecursive(head))
