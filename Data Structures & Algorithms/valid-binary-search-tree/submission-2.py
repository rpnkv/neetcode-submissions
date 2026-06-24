# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], lower=-1001, higher=1001) -> bool:
        if root.val <= lower or root.val >= higher:
            return False
       
        if not root.left:
            left_valid = True
        else:
            left_valid = self.isValidBST(root.left, lower, min(higher, root.val))
        
        if not root.right:
            right_valid = True
        else:
            right_valid = self.isValidBST(root.right, max(lower, root.val), higher)

        return left_valid and right_valid


