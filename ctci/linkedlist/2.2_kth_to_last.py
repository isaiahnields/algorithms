def kth_to_last(k, l):
    probe = l
    while probe and k > 0:
        probe = probe.next
        k -= 1

    if k: raise IndexError

    while probe:
        l = l.next
        probe = probe.next

    return l

from ctci.linkedlist import generate
from random import randint

for i in range(5):
    head = generate.generate_linked_list(i)
    idx = randint(0, i)
    print(head, idx)
    print(kth_to_last(idx, head))