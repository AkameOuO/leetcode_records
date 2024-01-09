# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeaves(root):
            if not root:
                return []
            
            return (getLeaves(root.left) + getLeaves(root.right)) or [root.val]
        return getLeaves(root1) == getLeaves(root2)