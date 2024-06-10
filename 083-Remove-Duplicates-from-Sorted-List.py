# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):

        p = head
        while head:
            if head.next and head.next.val == head.val:
                head.next = head.next.next
            else:
                head = head.next
        return p


# list = [1, 1, 2, 2, 3, 4, 5, 5]
# print(Solution().deleteDuplicates(list))

result1 = ListNode([1, 1, 2, 3, 3])

result = Solution()
print(result.deleteDuplicates(result1))
