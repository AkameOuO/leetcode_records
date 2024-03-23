# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        arr = []
        while cur:
            arr.append(cur.val);
            cur = cur.next
        
        index = 0
        while head:
            head.val = arr[index]
            if index >= 0:
                index += 1
            index *= -1
            head = head.next