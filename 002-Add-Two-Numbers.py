class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, list1, list2):
        result = ListNode(0)
        cur = result
        carry = 0

        while list1 or list2:
            val = carry
            if list1:
                val += list1.val
                list1 = list1.next
            if list2:
                val += list2.val
                list2 = list2.next
            cur.next = ListNode(val % 10)
            cur = cur.next
            carry = int(val / 10)

        if carry > 0:
            cur.next = ListNode(carry)
        return result.next


if __name__ == '__main__':
    a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
    data = Solution().addTwoNumbers(a, b)
    print(data.val, data.next.val, data.next.next.val)
