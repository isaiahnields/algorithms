from random import randint


class ListNode:

    def __init__(self, val):
        self.next = None
        self.val = val

    def __str__(self):
        curr = self
        result = []
        while curr:
            result.append(curr.val)
            curr = curr.next
        return '->'.join(str(i) for i in result)


def generate_linked_list(length):
    result = curr = ListNode(None)
    for i in range(length):
        curr.next = ListNode(randint(0, length))
        curr = curr.next
    return result.next