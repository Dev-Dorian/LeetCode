class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution(object):
    def hasCycle(self, head):
        fast = head

        while fast and fast.next:
            head = head.next
            fast = fast.next.next
            if head is fast:
                return True
        return False


if __name__ == "__main__":
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)

    print(Solution().hasCycle(head))
