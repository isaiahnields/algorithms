from ctci.linkedlist import generate
import time

# O(n) time and O(n) space
def remove_duplicates(head):
    seen = set()
    prev = None
    while head:
        if head.val in seen:
            prev.next = head.next
        else:
            seen.add(head.val)
            prev = head
        head = head.next


# O(n^2) time and O(1) space
def remove_duplicates(head):
    while head:
        runner = head
        while runner and runner.next:
            if runner.next.val == head.val:
                runner.next = runner.next.next
            else:
                runner = runner.next

        head = head.next


def verify(head):
    seen = set()
    while head:
        if head.val in seen:
            return False
        seen.add(head.val)
        head = head.next
    return True

average = []
for i in range(1):
    head = generate.generate_linked_list(5000)
    start = time.time()
    remove_duplicates(head)
    end = time.time()
    average.append(end - start)
    assert verify(head)

print(sum(average) / len(average))
