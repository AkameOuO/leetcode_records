# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        r = []
        while head:
            if head.val == 0:
                head = head.next
                continue
            try:
                i = l.index(-head.val)
                l[i:] = []
                r[i:] = []
                l = list(map(lambda x:x+head.val,l))
            except:
                l.append(0)
                l = list(map(lambda x:x+head.val,l))
                r.append(head)
            head = head.next
        if not r:
            return None
        for i in range(len(r)-1):
            r[i].next = r[i+1]
        r[-1].next = None
        return r[0]