class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution(object):
    def Merge_Two_Sorted_Lists(self, list1, list2):

        head = ListNode()
        current = head
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 or list2
        return head.next


if __name__ == "__main__":

    list1 = ListNode(1)
    list1.next = ListNode(3)
    list1.next.next = ListNode(5)
    list1.next.next.next = ListNode(6)
    list1.next.next.next.next = ListNode(8)

    list2 = ListNode(2)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)

    print(Solution().Merge_Two_Sorted_Lists(list1, list2))
