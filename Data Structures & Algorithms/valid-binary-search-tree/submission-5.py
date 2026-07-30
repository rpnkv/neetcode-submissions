# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], lower=-1001, higher=1001) -> bool:
        if not root:
            return True
        
        if root.val <= lower or root.val >= higher:
            return False
        
        return (self.isValidBST(root.left, lower = lower, higher = root.val) and
        self.isValidBST(root.right, lower = root.val, higher = higher))