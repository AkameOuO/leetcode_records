# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max = 0
    
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.trace(root,root.val,root.val)
        return self.max
    
    def trace(self,root,curmin,curmax):
        if not root:
            return
        self.max = max(self.max,abs(curmin-root.val),abs(curmax-root.val))
        self.trace(root.left,min(curmin,root.val),max(curmax,root.val))
        self.trace(root.right,min(curmin,root.val),max(curmax,root.val))