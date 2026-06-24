# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and q) or (p and not q) or (not p and not q):
            return False

        if p.val != q.val:
            return False

        if not p.left and not q.left:
            left_eq = True
        else:
            left_eq = self.isSameTree(p.left, q.left) 
        
        if not p.right and not q.right:
            right_eq = True
        else:
            right_eq = self.isSameTree(p.right, q.right)
    

        return left_eq and right_eq