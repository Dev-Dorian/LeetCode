class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution:
def getIntersectionNode(headA, headB):

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
    listB.next.next.next.next.next = ListNode(5)\

    listB.next.next.next = listA.next.next

    print(getIntersectionNode(listA, listB).val)
    """ intersectionPoint = getIntersectionNode(listA, listB)

    if intersectionPoint is None:
        print("-1")
    else:
        print(intersectionPoint.val)
 """
