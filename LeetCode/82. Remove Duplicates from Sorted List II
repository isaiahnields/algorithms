# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = sent = ListNode(0)
        sent.next = head
        while curr and curr.next and curr.next.next:
            dup = False
            if curr.next.val == curr.next.next.val:
                probe = curr.next.next
                dup = True
                while probe and probe.val == curr.next.val:
                    probe = probe.next
                curr.next = probe
            if not dup:
                curr = curr.next  
        return sent.next
