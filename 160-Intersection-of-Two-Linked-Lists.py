class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):

        res = set()
        while headA != None:
            res.add(headA)
            headA = headA.next
        while headB != None:
            if headB in res:
                return headB
            headB = headB.next


if __name__ == "__main__":
    listA = ListNode(4)
    listA.next = ListNode(1)
    listA.next.next = ListNode(8)
    listA.next.next.next = ListNode(4)
    listA.next.next.next.next = ListNode(5)

    listB = ListNode(5)
    listB.next = ListNode(6)
    listB.next.next = ListNode(1)
    listB.next.next.next = ListNode(8)
    listB.next.next.next.next = ListNode(4)
    listB.next.next.next.next.next = ListNode(5)

# listA = [4, 1, 8, 4, 5]
# listB = [5, 6, 1, 8, 4, 5]
    print(Solution().getIntersectionNode(listA, listB))
