class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head: ListNode) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


class Solution_1(object):
    def isPalindrome_1(self, head: ListNode) -> bool:
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        i, j = 0, len(ans) - 1
        while i < j:
            if ans[i] != ans[j]:
                return False
            i, j = i + 1, j - 1
        return True


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    print(Solution().isPalindrome(head))
    print(Solution_1().isPalindrome_1(head))
