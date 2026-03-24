class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for index in range(1, len(arr)):
        curr.next = ListNode(arr[index])
        curr = curr.next
    return head


def print_list(node):
    res = []
    while node:
        res.append(str(node.val))
        node = node.next
    print(" -> ".join(res))


def partition(head, x):
    before_dummy = ListNode(0)
    after_dummy = ListNode(0)

    before = before_dummy
    after = after_dummy

    curr = head
    while curr:
        if curr.val < x:
            before.next = curr
            before = before.next
        else:
            after.next = curr
            after = after.next
        curr = curr.next
    after.next = None
    before.next = after_dummy.next

    return before_dummy.next


head = [1, 4, 3, 2, 5, 2]
x = 3

linked_list_head = create_linked_list(head)
print_list(linked_list_head)

sorted_head = partition(linked_list_head, x)
print_list(sorted_head)
