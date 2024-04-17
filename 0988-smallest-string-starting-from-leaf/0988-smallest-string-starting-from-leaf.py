# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = "{"
        def dfs(cur,s=""):
            nonlocal res
            if not cur:
                return
            s = chr(cur.val+97) + s
            if not cur.left and not cur.right:
                if s < res:
                    res = s
            dfs(cur.left,s)
            dfs(cur.right,s)
        dfs(root)
        return res