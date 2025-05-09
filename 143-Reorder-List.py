class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution(object):
    def reorderList(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        act = slow.next  # Point to the first node of the second half
        slow.next = None  # Don't detach the second half (correction)
        while act:
            tmp = act.next
            act.next = prev
            prev = act
            act = tmp
        act = head

        while prev:
            t = prev.next
            prev.next = act.next
            act.next = prev
            act, prev = prev.next, t

        return head  # Return the modified head

    def reorderList1(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        act = slow.next  # Point to the first node of the second half
        prev = None
        slow.next = None
        # Don't detach the second half (correction)
        while act:
            tmp = act.next
            act.next = prev
            prev = act
            act = tmp

        a = head
        b = prev
        while b:
            tmp1 = a.next
            tmp2 = b.next
            a.next = b
            b.next = tmp1
            a = tmp1
            b = tmp2

        return head

    def reorderList2(self, head):
        if not head or not head.next:
            return

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        first, second = head, prev
        while second.next:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        return head


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(Solution().reorderList2(head))
