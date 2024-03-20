# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cur = head = ListNode(0,list1)
        for i in range(a):
            cur = cur.next
        t = cur.next
        cur.next = list2
        while cur.next:
            cur = cur.next
        for i in range(a,b):
            t = t.next
        cur.next = t.next
        return head.next