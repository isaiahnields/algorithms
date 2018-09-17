# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        return self.mergeSort(head)
        
        
    def mergeSort(self, head):
        if not head.next:
            return head
        
        left = head
        right = self.findCenter(head)
        
        left = self.mergeSort(left)
        right = self.mergeSort(right)
        return self.merge(left, right)
        
        
    def merge(self, l, r):
        sentinal = result = ListNode(0)
        while l and r:
            if l.val < r.val:
                result.next = l
                l = l.next
            else:
                result.next = r
                r = r.next
            result = result.next
            
        if l:
            result.next = l
        elif r:
            result.next = r
            
        return sentinal.next
            
        
    def findCenter(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        center = slow.next
        slow.next = None
        return center 
